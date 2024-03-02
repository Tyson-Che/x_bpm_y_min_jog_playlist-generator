# Jogging Playlist Creator

Create your personalized jogging playlist with the desired BPM and session duration using your own music collection and a running steps sound effect. The `JoggingPlaylistCreator` is a Python script that combines music tracks from a specified directory, adjusts a running steps sound effect to your jogging BPM, and mixes both to generate a continuous jogging playlist.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourrepository/JoggingPlaylistCreator.git
   cd JoggingPlaylistCreator
   ```

2. **Install Dependencies**

   Make sure you have Python 3.6 or later installed on your system. Then, install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare Your Music and Sound Effect Files**

   - Place your MP3 music tracks in a directory of your choice. These tracks will be combined into your jogging playlist.
   - Download a running steps sound effect clip and trim it to ensure it can be looped effectively. The clip should be short and able to be divided into an integer number of beats.

2. **Configure the Script**

   Open the `JoggingPlaylistCreator.py` script in your favorite text editor and set the following variables at the top of the script:

   - `music_directory`: Path to the directory containing your music tracks.
   - `steps_clip_path`: Path to your trimmed running steps sound effect clip.
   - `output_bpm`: Desired BPM (beats per minute) for your jogging session.
   - `session_duration_minutes`: Length of your jogging session in minutes.

3. **Run the Script**

   Execute the script to generate your jogging playlist:

   ```bash
   python JoggingPlaylistCreator.py
   ```

   The final jogging playlist will be saved in the specified output directory with the name `final_jogging_playlist.mp3`.

## Requirements

- Python 3.6 or later
- [pydub](https://github.com/jiaaro/pydub)
- [librosa](https://librosa.github.io/librosa/)
- [numpy](https://numpy.org/)

These dependencies are listed in the `requirements.txt` file and can be installed using pip as shown in the Installation section.

## Customization

You can customize the generated jogging playlist by adjusting the `output_bpm` and `session_duration_minutes` variables in the script. Additionally, you can replace the music tracks and running steps sound effect clip with your own choices to further personalize your playlist.

## Troubleshooting

- Ensure all MP3 files are not corrupted and are properly encoded.
- Verify that the running steps sound effect clip is trimmed correctly and loops seamlessly.
- If you encounter errors related to file paths, confirm that all specified paths in the script are correct and accessible.

For further assistance, please open an issue on the GitHub repository page.

## Contributing

Contributions to the `JoggingPlaylistCreator` are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

