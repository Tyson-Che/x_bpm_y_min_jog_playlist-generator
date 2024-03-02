# jogging_playlist_creator.py

from pydub import AudioSegment
import os
import librosa
import numpy as np

class JoggingPlaylistCreator:
    def __init__(self, music_directory, steps_clip_path, output_bpm, session_duration_minutes):
        self.music_directory = music_directory
        self.steps_clip_path = steps_clip_path
        self.output_bpm = output_bpm
        self.session_duration_minutes = session_duration_minutes

    def combine_mp3s(self, output_file='all.mp3'):
        combined = AudioSegment.empty()
        for file in os.listdir(self.music_directory):
            if file.endswith(".mp3"):
                sound = AudioSegment.from_mp3(os.path.join(self.music_directory, file))
                combined += sound
        combined.export(output_file, format="mp3")

    def calculate_and_adjust_bpm(self, target_bpm):
        y, sr = librosa.load(self.steps_clip_path, sr=None)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        original_bpm = np.mean(tempo)

        clip = AudioSegment.from_file(self.steps_clip_path)
        playback_speed = target_bpm / original_bpm
        adjusted_clip = clip._spawn(clip.raw_data, overrides={
            "frame_rate": int(clip.frame_rate * playback_speed)
        }).set_frame_rate(clip.frame_rate)

        return adjusted_clip

    def create_continuous_metronome(self, adjusted_clip):
        total_duration_ms = self.session_duration_minutes * 60 * 1000
        continuous_metronome = AudioSegment.silent(duration=total_duration_ms)

        current_position_ms = 0
        while current_position_ms < total_duration_ms:
            continuous_metronome = continuous_metronome.overlay(adjusted_clip, position=current_position_ms)
            current_position_ms += len(adjusted_clip)

        return continuous_metronome

    def mix_tracks(self, music_track_path, metronome_track, output_file='final_jogging_playlist.mp3'):
        music_track = AudioSegment.from_mp3(music_track_path)
        final_mix = music_track.overlay(metronome_track)
        final_mix.export(output_file, format="mp3")

# Note: The actual instantiation and usage of this class should handle the specific paths, BPM, and duration values.
