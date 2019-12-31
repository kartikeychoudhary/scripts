# Scripts

## Imgur
Imgur is a website where anyone can upload images or host image

Upload images using the following :

    Use -f 'path' : To upload image from path 
    Use -d 'directory' : To upload images from directory
    Use -help for help
    
    example : python main.py -f test.png
    
This will create a JSON file with the uploaded images details along with the direct links

## Google_OCR
It is a tool which will convert your images to text

Convert images using the following :

    Use -f 'path' : To convert image from path 
    Use -d 'directory' : To convert images from directory
    Use -help for help
    
    example : python main.py -f test.png
    
This will create a TXT file with the images name

## Zippyshare Downloader 
It is a tool download or get download links for zippyshare website
Run setup.sh to configure your system linux user only else script works on both windows(need to setup selenium) and linux


using the following commands:

    Use -l 'link' : To download from single link
    Use -f 'path' : To download files from the links provided in a file path given
    Use -fs 'path' : To get Download links in the result.txt
    Use -help for help
    
    example : python main.py -f < LINK URL >
    
This will help you download files from zippyshare or save links to download using diffrent software

## Rearrange your data
It is a tool to arrange all the data in a directory to the respective dataType Folders : Documents, Images, Videos, etc can be added easily just changes to be done in the dictionary.

    Use Python rearrange.py [SOURCE PATH] [DESTINATION PATH] # PUT FULL PATH ( only for linux )
    
    example : python rearrange.py /home/user/Downloads /dev/sda1/Downloads 
