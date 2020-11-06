Welcome

In this repository are two folders: scripts and training files.
Folder "script" contains script written in python that gets eps files as input, such files are in training files folder, and reads numbers written in those files.
Folder "training files" contains eps files on which OCR.py script was tested.

To run OCR.py script you need to configure your environment properly.
1. Running python script requires python interpreter. Writing this script I used Anaconda which provides interpreter and allows to easily download additional libraries. It can be found on this site: https://www.anaconda.com/products/individual.
2. If you downloaded and installed Anaconda package here are the next steps.\
2.1. Run Anaconda Prompt (Anaconda3).\
2.2. Create new environment using command: conda create -n name (name is name of your environment).\
2.3. You can now enter your environment using command: conda activate name. When you activate environmet the line\
2.4. Now that you've entered your created environment you can install packages needed to run script. \
These packages are: \
      -numpy: command: conda install -c conda-forge numpy, \
      -opencv: command: conda install -c conda-forge opencv, \
      -pytesseract: commang: conda install -c conda-forge pytesseract.\
3. After you successfully installed these packages download script and prepare images you want to pass to script.\
4. Navigate to folder where OCR.py and images are stored. You can do it using command: cd.\
5. To execute the script write in command prompt line similar to: python OCR.py train_1.eps train_2.eps train_3.eps etc.\
   You can use as many eps files as you like with different names.\
6. In command prompt you should get results of running this script.\
