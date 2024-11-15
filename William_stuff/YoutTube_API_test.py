# -*- coding: utf-8 -*-

# Sample Python code for youtube.comments.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os, json

#NOTE: download required libraries
# https://developers.google.com/youtube/v3/quickstart/python

# pip install --upgrade google-api-python-client

# pip install --upgrade google-auth-oauthlib google-auth-httplib2

import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = ""
    # NOTE: Get API key from https://console.cloud.google.com/apis/credentials/key/7cdafeaf-9d93-438b-9166-a04dfc27a1bc?authuser=1&inv=1&invt=Abhksg&project=eecs498-project

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.comments().list(
        part="snippet",
        parentId="UgzDE2tasfmrYLyNkGt4AaABAg"
    )
    response = request.execute()
    
    f = open('data.json', 'w', encoding='utf-8')
    json.dump(response, f, ensure_ascii=False, indent=4)

    print(response)

def main2():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyB6kyShoh7IQG9_nHTPkgX19x-IKrxzBR4"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        type='video',
        videoLicense="creativeCommon",
        q="obama and trump minecraft" #NOTE: Key word to search
        # parentId="UgzDE2tasfmrYLyNkGt4AaABAg"
    )
    response = request.execute()
    
    f = open('data.json', 'w', encoding='utf-8')
    json.dump(response, f, ensure_ascii=False, indent=4)

    # print(response)

if __name__ == "__main__":
    # main()
    main2()
    f = open('data.json')
    searchResult = json.load(f)
    videos = searchResult['items']
    for video in videos:
        #https://www.youtube.com/watch?v=
        print(video['id']['videoId'])
