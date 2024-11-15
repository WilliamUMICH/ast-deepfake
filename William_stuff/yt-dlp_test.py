import subprocess

#yt-dlp  -x --audio-format mp3 --write-subs "https://www.youtube.com/watch?v=KBcxuM-qXec" #NOTE: this is the command to download video via CLI

url = "https://www.youtube.com/watch?v=KBcxuM-qXec"

subprocess.run(['yt-dlp', '-x', '--audio-format', 'mp3', '--write-subs', url], capture_output=True, text=True)


#yt-dlp -x --audio-format mp3 --write-subs --write-auto-subs --sub-lang en -P ./videoData "https://www.youtube.com/watch?v=yP89N7zzreQ"
