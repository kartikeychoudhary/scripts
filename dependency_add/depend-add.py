import os
import json
from datetime import datetime
import sys
import argparse

WORKING_PATH = ''


def dir_path(path):

    if path == '.':
        return os.getcwd()

    if os.path.isdir(path):
        return path
    else:
        if os.path.isdir(os.getcwd()+path):
            return os.getcwd()+path
        else:
            raise NotADirectoryError(path)
        raise NotADirectoryError(path)


def add_html(path):
    if not os.path.exists(path+"/index.html"):
        os.system("cp index.html "+path)
    else:
        print("index.html exists ... \n")


def add_to_html(path, data):
    print("adding : " + data)
    temp = ''
    with open(path+'/index.html', 'r') as f:
        temp = f.read()
        f.close()
    loc = temp.find("</head>")
    temp = temp[:loc] + data + temp[loc:]
    with open(path+'/index.html', 'w') as f:
        f.write(temp)
        f.close()


def add_to_app_js(path, data):
    temp = ''
    with open(path+'/src/App.js', 'r')as f:
        temp = f.read()
        f.close()
    temp = data + temp
    with open(path + '/src/App.js', 'w')as f:
        f.write(temp)
        f.close()


def bootstrap(path):
    print("Adding Bootstrap to you project at :" + path + "\n")
    add_html(path)
    add_to_html(path, "<link rel='stylesheet' href='css/bootstrap.min.css'/>")
    add_to_html(path, "<script src='js/bootstrap.min.js' ></script>")
    os.system("cp -r static/bootstrap/* "+path)


def bootstrapscss(path):
    print("Adding Bootstrap-SCSS to you project at :" + path + "\n")
    add_html(path)
    add_to_html(path, "<link rel='stylesheet' href='css/bootstrap.min.css'/>")
    add_to_html(path, "<script src='js/bootstrap.min.js' ></script>")
    os.system("cp -r static/bootstrap.scss/* " + path)


def fontawesome(path):
    print("Adding FontAwesome to you project at at :" + path)
    add_html(path)
    add_to_html(path, "<link rel='stylesheet' href='css/fontawesome.min.css'/>")
    add_to_html(path, "<script src='js/fontawesome.min.js'></script>")
    os.system("cp -r static/fontawesome/* " + path)


def fonstawesomescss(path):
    print("Adding FontAwesome-SCSS to you project at :" + path)
    add_html(path)
    add_to_html(path, "<link rel='stylesheet' href='css/fontawesome.min.css'/>")
    add_to_html(path, "<script src='js/fontawesome.min.js'></script>")
    os.system("cp -r static/fontawesome.scss/* " + path)


def jquery(path):
    print("Adding jquery to you project at :" + path)
    add_html(path)
    add_to_html(path, "<script src='js/jquery-1.12.4.min.js'></script>")
    os.system("cp -r static/jquery/* " + path)


def scss(path):
    print("Adding scss to you project at :" + path)
    add_html(path)
    add_to_html(path, "<link rel='stylesheet' href='css/style.css'/>")
    os.system("cp -r static/scss/* " + path)


def htmltemplate(path):
    print("Adding HTML template to your directory :" + path)
    add_html(path)
    bootstrap(path)
    fontawesome(path)


def reactbootstrap(path):
    print("Adding Bootstrap to your project at :" + path + "\n")
    os.system("cd " + path + " && " + "npm install bootstrap --save")
    add_to_app_js(path, "import 'bootstrap/dist/css/bootstrap.min.css';\n")


def reactfontawesome(path):
    print("Adding FontAwesome to your project at :" + path + "\n")
    # os.system("cd " + path + " && " + "npm install fontawesome --save")
    # add_to_app_js(path, "import 'fontawesome/css/fontawesome.min.css';\n")
    # https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css
    # https://use.fontawesome.com/releases/v5.1.1/css/all.css
    add_to_html(path+"/public",
                "<link rel='stylesheet' href='https://use.fontawesome.com/releases/v5.1.1/css/all.css'/>")


def reactredux(path):
    print("Adding Redux to your project at :" + path + "\n")
    os.system("cd " + path + " && " + "npm install --save react-redux redux")
    add_to_app_js(path, "import { Provider } from 'react-redux';\n")
    # print("ADDED")


def reactrouterdom(path):
    print("Adding react-router-dom to your project at :" + path + "\n")
    os.system("cd " + path + " && " + "npm install --save react-router-dom")
    add_to_app_js(
        path, "import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';\n")
    # print("ADDED")


def reactReduxFirebaseConfig(path):
    print("Adding Redux Firebase with Firestore, Auth to your project at :" + path + "\n")
    os.system("cd " + path + " && " +
              "npm install --save firebase react-redux-firebase redux redux-auth-wrapper redux-firestore react-redux")
    add_to_app_js(path, "import { Provider } from 'react-redux';\n")
    # print("ADDED")


def angulartemplate(path):
    print("Adding Angular template to your directory :" + path)


def helpPrint():
    msg = "Welcome to Automation Script to Add Web Dependencies \n\n " \
          "Use --bootstrap : To add Bootstrap to your project  \n " \
          "Use --bootstrap-scss : to add Bootstrap SCSS to your project \n " \
          "Use --fontawesome : to add FontAwesome to your project \n " \
          "Use --fontawesome-scss : to add FontAwesome SCSS to your project \n " \
          "Use --jquery : to add JQuery to your project \n " \
          "Use --scss : to add SCSS template to your project \n " \
          "Use --html : to add SCSS template to your project \n "

    return msg


def main():
    parser = argparse.ArgumentParser(
        description=helpPrint())
    # parser.add_argument(
    #     'path',  type=dir_path, help='allowed parameter')
    parser.add_argument(
        '-b', '--bootstrap',  type=dir_path, help='with Path to add Bootstrap')
    parser.add_argument(
        '-bs', '--bootstrap-scss', type=dir_path, help='with Path to add Bootstrap with SCSS')
    parser.add_argument(
        '-f', '--fontawesome',  type=dir_path, help='with Path to add FontAwesome')
    parser.add_argument(
        '-fs', '--fontawesome-scss',  type=dir_path, help='with Path to add FontAwesome with SCSS')
    parser.add_argument(
        '-j', '--jquery', type=dir_path, help='with Path to add jquery')
    parser.add_argument(
        '-s', '--scss', type=dir_path, help='with Path to add scss')
    parser.add_argument(
        '-ht', '--html', type=dir_path, help='with Path to add html')
    parser.add_argument(
        '-rb', '--react-bootstrap', type=dir_path, help='with Path to add Bootstarp to react')
    parser.add_argument(
        '-rf', '--react-fontawesome', type=dir_path, help='with Path to add FontAwesome to react')
    parser.add_argument(
        '-rr', '--react-redux', type=dir_path, help='with Path to add Redux to react')
    parser.add_argument(
        '-rrd', '--react-router-dom', type=dir_path, help='with Path to add React Router Dom to react')
    parser.add_argument(
        '-rfc', '--react-firebase-config', type=dir_path, help='with Path to add Redux Firebase with Auth and Firestore to react')

    args = parser.parse_args()
    if args.bootstrap != None:
        bootstrap(args.bootstrap)
    elif args.bootstrap_scss != None:
        bootstrapscss(args.bootstrap_scss)
    elif args.fontawesome != None:
        fontawesome(args.fontawesome)
    elif args.fontawesome_scss != None:
        fontawesome(args.fontawesomescss)
    elif args.jquery != None:
        jquery(args.jquery)
    elif args.scss != None:
        scss(args.scss)
    elif args.html != None:
        htmltemplate(args.html)
    elif args.react_bootstrap != None:
        reactbootstrap(args.react_bootstrap)
    elif args.react_fontawesome != None:
        reactfontawesome(args.react_fontawesome)
    elif args.react_redux != None:
        reactredux(args.react_redux)
    elif args.react_router_dom != None:
        reactrouterdom(args.react_router_dom)
    elif args.react_firebase_config != None:
        reactReduxFirebaseConfig(args.react_firebase_config)


if __name__ == "__main__":
    # print("test")
    main()
