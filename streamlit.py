{ kkkkk
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0637220c-9ec3-4c92-93b9-a0cd7d1006e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: openai in c:\\users\\hp\\anaconda3\\lib\\site-packages (1.79.0)\n",
      "Requirement already satisfied: streamlit in c:\\users\\hp\\anaconda3\\lib\\site-packages (1.37.1)\n",
      "Requirement already satisfied: pillow in c:\\users\\hp\\anaconda3\\lib\\site-packages (10.4.0)\n",
      "Collecting pytesseract\n",
      "  Downloading pytesseract-0.3.13-py3-none-any.whl.metadata (11 kB)\n",
      "Collecting pdf2image\n",
      "  Downloading pdf2image-1.17.0-py3-none-any.whl.metadata (6.2 kB)\n",
      "Requirement already satisfied: anyio<5,>=3.5.0 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from openai) (4.8.0)\n",
      "Requirement already satisfied: distro<2,>=1.7.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from openai) (1.9.0)\n",
      "Requirement already satisfied: httpx<1,>=0.23.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from openai) (0.28.1)\n",
      "Requirement already satisfied: jiter<1,>=0.4.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from openai) (0.10.0)\n",
      "Requirement already satisfied: pydantic<3,>=1.9.0 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from openai) (2.10.6)\n",
      "Requirement already satisfied: sniffio in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from openai) (1.3.1)\n",
      "Requirement already satisfied: tqdm>4 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from openai) (4.66.5)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.11 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from openai) (4.12.2)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from streamlit) (5.3.3)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: numpy<3,>=1.20 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (24.2)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from streamlit) (2.1.4)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (5.29.0)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from streamlit) (16.1.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (2.32.3)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (13.9.4)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from streamlit) (8.2.3)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from streamlit) (3.1.43)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (6.4.2)\n",
      "Requirement already satisfied: watchdog<5,>=2.1.5 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from streamlit) (4.0.1)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
      "Requirement already satisfied: toolz in c:\\users\\hp\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: idna>=2.8 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from anyio<5,>=3.5.0->openai) (3.10)\n",
      "Requirement already satisfied: colorama in c:\\users\\hp\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: certifi in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from httpx<1,>=0.23.0->openai) (2024.8.30)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\hp\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->openai) (1.0.2)\n",
      "Requirement already satisfied: h11<0.15,>=0.13 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai) (0.14.0)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: annotated-types>=0.6.0 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from pydantic<3,>=1.9.0->openai) (0.7.0)\n",
      "Requirement already satisfied: pydantic-core==2.27.2 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from pydantic<3,>=1.9.0->openai) (2.27.2)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from requests<3,>=2.27->streamlit) (3.4.0)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from requests<3,>=2.27->streamlit) (2.2.3)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.22.3)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\hp\\appdata\\roaming\\python\\python312\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
      "Downloading pytesseract-0.3.13-py3-none-any.whl (14 kB)\n",
      "Downloading pdf2image-1.17.0-py3-none-any.whl (11 kB)\n",
      "Installing collected packages: pytesseract, pdf2image\n",
      "Successfully installed pdf2image-1.17.0 pytesseract-0.3.13\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install openai streamlit pillow pytesseract pdf2image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37b85acf-2692-41d9-a99d-f3e5c96402b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "from PIL import Image\n",
    "import pytesseract\n",
    "from pdf2image import convert_from_path\n",
    "from openai import OpenAI\n",
    "import os\n",
    "st.set"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
