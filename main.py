import yt_dlp

# playlist_toggle = input('Is it a playlist? Write "True" or "False":\n')
# while playlist_toggle != "True" and playlist_toggle != "False":
#    playlist_toggle = input('Invalid input, please write "True" or "False"\n')

format = input("Choose one of the formats for converting (.mp3 .wav):\n")
while format != ".mp3" and format != ".wav":
    format = input("Invalid option, please enter another format:\n")


def download_video_as_mp3(video_url, save_path="loot/"):
    # Define the options for yt-dlp
    ydl_opts = {
        "noplaylist": False,  # bool(playlist_toggle),
        "outtmpl": save_path + "%(title)s.%(ext)s",  # Save with the video title
        "postprocessors": [
            {  # Post-process to convert audio to MP3
                "key": "FFmpegExtractAudio",
                "preferredcodec": format,  # Convert to MP3 format
                "preferredquality": "320",  # Use high quality (320 kbps)
            }
        ],
    }

    # Use yt-dlp to download and convert the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


# Example usage
url = input("URL here: ")
download_video_as_mp3(url)
