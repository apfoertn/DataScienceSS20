{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Exercise1a.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyO9OnyGWeF5MnvxWBvZX0gu",
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
        "<a href=\"https://colab.research.google.com/github/apfoertn/DataScienceSS20/blob/Block_1/Exercise1a.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2-bkkX_oLVSC",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "list = ListKeeper()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gU2HYcMkLeQ1",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 33
        },
        "outputId": "c7d767fe-a6f1-4c73-9878-c58a49c7ac3a"
      },
      "source": [
        "print(list.list)\n"
      ],
      "execution_count": 115,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'example': [1, 2, 3, 4, 5]}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3Oxcq0MdMLde",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 33
        },
        "outputId": "ca941761-21fa-4041-861b-290e18c56603"
      },
      "source": [
        "list.show()"
      ],
      "execution_count": 116,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "dict_keys(['example'])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 116
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2hOrk_UBMRDp",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "list.add('abc', [3,4,5,6])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EjlO--YIMfMb",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 33
        },
        "outputId": "dac62cec-ccc2-4f27-c40d-3f89eb20c9e9"
      },
      "source": [
        "list.show()"
      ],
      "execution_count": 118,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "dict_keys(['example', 'abc'])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 118
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "t7FazlxWMk0e",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "list.add('def', [5,3,7,8])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XCP7--ojOTIS",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 33
        },
        "outputId": "7eb36ad1-e0d1-4283-d3ba-0da31e0e1de4"
      },
      "source": [
        "list.show()"
      ],
      "execution_count": 120,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "dict_keys(['example', 'abc', 'def'])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 120
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HcvIqCqrOUiu",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 33
        },
        "outputId": "8bb5770c-4669-46e7-afc8-23061cb3a518"
      },
      "source": [
        "list.sort('def')"
      ],
      "execution_count": 121,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[3, 5, 7, 8]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 121
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4rfDAZ51Ww1o",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 33
        },
        "outputId": "ff010fcf-a623-42da-c51f-91f846dfdacf"
      },
      "source": [
        "list.append('def', [3,2,1])"
      ],
      "execution_count": 125,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[3, 5, 7, 8, [3, 2, 1], [3, 2, 1]]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 125
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OoAUTfDTYTuh",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}
