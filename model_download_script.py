'''

Please make sure the environment which you install the API.
Executing this script to download the pretrained phonlp model for further convenience.
The script would download the model file to the current folder. 
If you want to place to another directory, please modify the path you want.

'''

import phonlp
import os, sys

phonlp.download('./')