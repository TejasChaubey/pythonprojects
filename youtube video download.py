print("WELCOME , TO MY PROGRAM THIS PROGRAM IS TO DOWNLOAD YOUTUBE VIDEOS/PLAYLISTS.")
n=int(input("if you want to download video than press 1:\n if download playlist press 2 :"))
if n==1:
    from pytube import YouTube
    link =input("PLEASE PASTE THE LINK OF VIDEO ,YOU WANT TO DOWNLOAD : ")
    youtube_1 = YouTube(link)
    print("press 1 for title \n press 2 for thumbnail \n press 3 for video/audio \n")
    num=int(input("Enter choice\n"))
    if num==1:
        print(youtube_1.title)
    if num==2:
        print(youtube_1.thumbnail_url)
    if num==3:    
        #videos = youtube_1.streams.all()      #  -->(THIS METHOD IS FOR KNOW ABOUT ALL STRING OF VIDEO)
        ch=int(input("press 1 for audio,\npress 2 for video"))
        if ch==1:
            videos = youtube_1.streams.filter(only_audio=True)
        if ch==2:
            videos = youtube_1.streams.all()
    video=list(enumerate(videos))
    for i in video:
        print(i)
    print()
    strm = int(input("ENTER YOUR CHOICE IN WHICH STREAM YOU WANT TO DOWNLOASD VIDEO : "))
    videos[strm].download()
print("YOUR VIDEO IS DOWNLOADED SUCCESFULLY, JUST GO AND ENJOY IT.")
if n==2:
    from pytube import Playlist
    link =input("PLEASE PASTE THE LINK OF PLAYLIST ,YOU WANT TO DOWNLOAD : ")
    playl = Playlist(link)
    print(f'Downloading : {playl.title}')
    for video in playl.videos:
        video.streams.first().download
    
