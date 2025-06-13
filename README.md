# 🎵 YouTube Alarm Clock

A fun command-line alarm clock application that wakes you up by playing a random YouTube video in your browser! 🎬⏰

## ✨ Features
- ⏰ Set alarm times in HH:MM or HH:MM:SS format
- 🎯 Randomly selects and plays YouTube videos when alarm triggers
- 📁 Load custom YouTube playlists from text files
- 🖥️ Both interactive and command-line modes
- ⚡ Real-time countdown display
- 🎨 Clean, user-friendly interface
- 📝 Sample YouTube links included


### Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/sainandan2005/Youtube-Alarm-Clock.git
   cd Youtube-Alarm-Clock
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the alarm clock:**
   ```bash
   python main.py
   ```

## 📖 Usage

### Interactive Mode

Launch the application and follow the prompts:

```bash
python main.py
```

The application will guide you through:
1. Setting up your YouTube links file
2. Configuring your alarm time
3. Starting the countdown

### Command Line Mode

For quick setup, use command line arguments:

```bash
python main.py -t 07:30 -f my_playlist.txt
```

**Options:**
- `-t, --time`: Alarm time in HH:MM or HH:MM:SS format
- `-f, --file`: Path to YouTube links file (optional)

### 📝 YouTube Links File

Create a text file with one YouTube URL per line:

```
https://youtu.be/2nP3ElUtFDU?si=VlNRqGGKddgC_EZU
https://youtu.be/-Djq3QihTyA?si=cqIFCf3kb7b3lIq0,
https://youtu.be/IpFX2vq8HKw?si=rnGvvjeEUDFZ50dC
```

A sample `youtube_links.txt` file is automatically created on first run.

## 💡 Examples

```bash
# Morning alarm with default playlist
python main.py -t 07:30

# Custom time with specific playlist
python main.py -t 16:45:30 -f motivational_videos.txt

# Interactive setup
python main.py
```

## 🔧 How It Works

1. **Load Phase**: Application reads YouTube URLs from your specified file
2. **Wait Phase**: Displays countdown timer until alarm time
3. **Alarm Phase**: Randomly selects and opens a YouTube video in your browser
4. **Cancel**: Press `Ctrl+C` anytime to cancel the alarm



## 🎯 Future Enhancements

- [ ] Multiple alarm support
- [ ] Custom alarm sounds
- [ ] Snooze functionality
- [ ] GUI interface
- [ ] Playlist validation
- [ ] Volume control
