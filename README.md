# CodexNapariViewer
VIEWER INSTALLATION AND INSTRUCTIONS TO RUN SCRIPT
1.	If you are running windows, download anaconda from: https://www.anaconda.com/products/individual#windows and make sure to download the latest anaconda installer under python 3.7 – 64 bit installer (if the windows OS is 64 bit). 

If you are running windows server, go to: https://repo.anaconda.com/archive/
and download the installer: Anaconda3-2019.10-Windows-x86_64.exe

2.	Once Anaconda is downloaded, install it with default settings and make sure you have selected Python 3.7 as default. After installation, open Anaconda navigator and create an environment by clicking on ‘+’ button. 

3.	Now, name the environment as CodexViewer and click on ‘Play’ button to open this environment in terminal mode. After doing so, navigate to the folder where you have downloaded the script file i.e. the Viewer.py file and requirements.txt file using “cd” command.
Make sure you have python and pip installed by typing in the following 2 commands:
 	python --version  this should display python version installed, which would be 3.7.x
 	pip –version  this should display the pip version installed to install dependencies

4.	Now, type the following command:
    	pip install -r requirements.txt

	For Unix/Mac users, please remove or comment out the following:
		pywin32==227
		pywin32-ctypes==0.2.0
This above will take a while to install all the necessary dependencies, once that is done type the following command:
	pip install pyqt5

After downloading that, you have all the dependencies necessary to run the viewer script now.

5.	Now, run the script using the following command:
 	python Viewer.py <<location of processed data>> <<montage file name>>

For example:
 	python Viewer.py C:\NolanLab\Viewer_testProcessedData reg001_montage.tif
	
	For Unix/Mac users, not that the direction of slashes are different on unix based systems. You can edit Viewer.py to correct this.

6.	The above script would now open the viewer with the reg001_montage.tif file open based on the markers specified in channelNames.txt present in the processed folder.

Things to Note:
1.	Napari does not work with Remote Desktop, so if you want to run your viewer script on a remote server from your personal machine, use teamviewer.
2.	Make sure you have Experiment.json and channelNames.txt file present inside the processed folder, if not the script will not work.
3.	Make sure there is a bestFocus folder present, containing all your montage tif files. If not the script will not work as expected. 
4.	You can modify the script to your needs, depending on your dataset, if you would like to analyze something specific.
