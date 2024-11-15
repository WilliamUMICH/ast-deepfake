# -*- coding: utf-8 -*-

# Sample Python code for youtube.comments.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os, json, subprocess

import googleapiclient.discovery

import socket
socket.setdefaulttimeout(30000)

def main2():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyB6kyShoh7IQG9_nHTPkgX19x-IKrxzBR4"
    #                AIzaSyB6kyShoh7IQG9_nHTPkgX19x-IKrxzBR4

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        type='video',
        # videoLicense="creativeCommon",
        maxResults=2,
        order='videoCount',
        q="obama and trump minecraft" #NOTE: Key word to search
        # parentId="UgzDE2tasfmrYLyNkGt4AaABAg"
    )
    response = request.execute()
    
    f = open('data.json', 'w', encoding='utf-8')
    json.dump(response, f, ensure_ascii=False, indent=4)

    print(response)

if __name__ == "__main__":
    # main()
    main2()
    f = open('data.json')
    searchResult = json.load(f)
    videos = searchResult['items']
    videoURLs = []
    for video in videos:
        newURL = 'https://www.youtube.com/watch?v=' + video['id']['videoId']
        videoURLs.append(newURL)
        
        print(newURL)

    for videoURL in videoURLs:
        cliResult = subprocess.run(['yt-dlp', '-x', 
        '--audio-format', 'mp3', '--write-subs', '--write-auto-subs', '--sub-langs', 'en', '-P', './videoData' , videoURL], 
        capture_output=True, text=True)

        print(cliResult)
