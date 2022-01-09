{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "try/except-clause.py",
      "provenance": [],
      "authorship_tag": "ABX9TyOMVDvQ8JZMIKKJb6Sx2wZf"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "KVWSuQvyLCSI"
      },
      "outputs": [],
      "source": [
        "astr = 'Hello Bob'\n",
        "try:\n",
        "   istr = int(astr)\n",
        "except:\n",
        "   istr = -1\n",
        "\n",
        "print('First',istr)\n",
        "\n",
        "astr = '123'\n",
        "try:\n",
        "   istr = int(astr)\n",
        "except:\n",
        "   istr = -1\n",
        "\n",
        "print('Second', istr)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = input('Enter 42 ')\n",
        "try:\n",
        "   rty = int(num)\n",
        "except:\n",
        "   rty = -1\n",
        "\n",
        "if rty > 0:\n",
        "   print('Your no. is ', rty)\n",
        "else:\n",
        "   print('What is that?')"
      ],
      "metadata": {
        "id": "NYUrJxEXOzbL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "num = input('Enter Forty Two ')\n",
        "try:\n",
        "   rty = int(num)\n",
        "except:\n",
        "   rty = -1\n",
        "\n",
        "if rty > 0:\n",
        "   print('Your no. is ', rty)\n",
        "else:\n",
        "   print('It is not a no.')"
      ],
      "metadata": {
        "id": "9yJXcCl8P3TT"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}