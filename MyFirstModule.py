{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Exercise1a.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyO25wTe8SxXcD8Mb6d9//yJ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/apfoertn/DataScienceSS20/blob/master/MyFirstModule.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0lXvQsBoGX0R",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "class ListKeeper ():\n",
        "\n",
        "    '''List wird als Dictionary deklariert'''\n",
        "    list = {}\n",
        "\n",
        "    def __init__(self):\n",
        "      self.list[\"example\"] = [1,2,3,4,5]\n",
        "\n",
        "    def show (self):\n",
        "      '''This function returns all list names'''\n",
        "      return self.list.keys()\n",
        "\n",
        "    def add (self, name, newlist):\n",
        "      '''This function adds a new list to the dictionary'''\n",
        "      self.list[name] = newlist\n",
        "\n",
        "    def delete (self, name):\n",
        "      '''This function deletes the list with the given name'''\n",
        "      self.list.pop(name)\n",
        "\n",
        "    def sort (self, name):\n",
        "      '''This function returns the list with the given name in a sorted order'''\n",
        "      self.list[name].sort()\n",
        "      return self.list[name]\n",
        "\n",
        "    def append (self, name, applist):\n",
        "      '''This functions appends a list to the list with the given name'''\n",
        "      self.list[name].append(applist)\n",
        "      return self.list[name]\n"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}