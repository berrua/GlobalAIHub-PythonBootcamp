{
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# Variables"
      ],
      "metadata": {
        "id": "y-OgHUM89bn2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "name = 'Berru'\n",
        "name"
      ],
      "metadata": {
        "id": "PNO2kUKu9fac",
        "outputId": "9cdba884-5e24-4e1b-f9fa-bab132eecd9f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Berru'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "age = 22\n",
        "age"
      ],
      "metadata": {
        "id": "RfoENYZF9o6q",
        "outputId": "6f911e2a-42a6-47a0-f646-547e2fd39ae0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "22"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(name)\n",
        "print(age)"
      ],
      "metadata": {
        "id": "axOiC0-E9xVH",
        "outputId": "14277a42-648b-4cda-c20e-41a6c1f924cb",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Berru\n",
            "22\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(type(name))\n",
        "print(type(age))"
      ],
      "metadata": {
        "id": "nFdZ0-oQ96Jf",
        "outputId": "1b16f598-e6e4-4d82-a93a-46977396526e",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'str'>\n",
            "<class 'int'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name = 'Berru'\n",
        "type(name)"
      ],
      "metadata": {
        "id": "iaV3YQ4j-Hy1",
        "outputId": "49f4f747-3202-4671-f39f-29763db702b8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "items = ['Apple', 1.49, 'Banana', 2.56, 'Berry', 3.45, 'Cherry', 2.03]\n",
        "print(items, type(items))"
      ],
      "metadata": {
        "id": "EMhDGfw0DqEx",
        "outputId": "c8f77415-c1e5-4723-e246-49a23af50840",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Apple', 1.49, 'Banana', 2.56, 'Berry', 3.45, 'Cherry', 2.03] <class 'list'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(items[6])"
      ],
      "metadata": {
        "id": "Gb8244euEs5b",
        "outputId": "5e9b183a-6501-41f4-d859-28b1689e2141",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cherry\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(items[1:5])"
      ],
      "metadata": {
        "id": "P4RR4gkOEmCF",
        "outputId": "315e25d1-5d47-44fd-d108-d6e4cd313106",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1.49, 'Banana', 2.56, 'Berry']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(items[3:])"
      ],
      "metadata": {
        "id": "ZoxCnO80E4Nm",
        "outputId": "52b73b9c-a7ae-4168-f0eb-3ede9c4f6b7e",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[2.56, 'Berry', 3.45, 'Cherry', 2.03]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(items[:3])"
      ],
      "metadata": {
        "id": "N8oGeTdEFE-p",
        "outputId": "abd623de-7882-488e-b114-c23b40f2635c",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Apple', 1.49, 'Banana']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "items[2] = 'Melon'\n",
        "print(items)"
      ],
      "metadata": {
        "id": "j0QVV78PFLMI",
        "outputId": "b9ce59d9-5de4-4573-8d28-25cb9fa9627b",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Apple', 1.49, 'Melon', 2.56, 'Berry', 3.45, 'Cherry', 2.03]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "age = 22\n",
        "print(age, type(age))"
      ],
      "metadata": {
        "id": "yhIKVHGyFyXA",
        "outputId": "40949d95-6b75-4a30-b996-5ae3fc61b02e",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "22 <class 'int'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "age = 22\n",
        "age += 0.5\n",
        "print(age, type(age))"
      ],
      "metadata": {
        "id": "Pu2GKBL4F6Ta",
        "outputId": "96b43d85-c943-401d-abfa-23f7dfb918fd",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "22.5 <class 'float'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "age = '22'\n",
        "print(type(age))"
      ],
      "metadata": {
        "id": "fyfbkoz3H9ut",
        "outputId": "c6e51c88-24e2-4700-8cd4-2002baede65c",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'str'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "age = int(age)\n",
        "print(age, type(age))"
      ],
      "metadata": {
        "id": "mYPalnTOIGew",
        "outputId": "f31c688c-d640-4352-ebce-7ddae5e58b55",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "22 <class 'int'>\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "collapsed_sections": [],
      "name": "01Variables",
      "toc_visible": true,
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}