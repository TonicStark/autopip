# Autopip
**Autopip** is an **executable tool**, providing help for *updating* python project's packages when changing to a *new version*.

## Set Up
### Build by Yourself
Download the ZIP Folder, or Clone the Repository with:
```
git clone https://github.com/TonicStark/autopip.git
```

Then install the dependencies in a virtualenv, you can create one via `python -m venv <name of the virtualenv>`, with:
```
pip install -r requirements.txt
```
In the *virtualenv*, run the following command:
```
pyinstaller --onefile .\autopip.py
```
this will **build** the `autopip.py` file, as a **single** *executable*.
When you finish the build process, you should a *repo* like this:
```
.
└── autopip/
    ├── dist
    ├── build
    ├── venv
    ├── .gitignore
    ├── autopip.py
    ├── autopip.spec
    ├── README.md
    └── requirements.txt
```
Inside the `dist/` you should have a **file**, `autopip.exe` which you can **execute** as a single program, without having to *activate* the *virtualenv* each time.

To use it in **every** path of your Sistem, you have to add the `.\autopip\dist\` folder to your *Computer Path*: [here](https://chlee.co/how-to-setup-environment-variables-for-windows-mac-and-linux/) there's a **guide** on how to do it.
## Download (Windows only)
Else, you can *download* in the **Release** section, the *builded* file, ready to be added to your *System Path* to **use it!**