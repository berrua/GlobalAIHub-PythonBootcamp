{
  "metadata": {
    "kernelspec": {
      "display_name": "Pyolite",
      "language": "python",
      "name": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "source": "# Variables",
      "metadata": {},
      "id": "c3e2e321-3197-4601-9d19-6a3ed9193978"
    },
    {
      "cell_type": "code",
      "source": "name = 'Berru'\nname",
      "metadata": {
        "trusted": true
      },
      "execution_count": 1,
      "outputs": [
        {
          "execution_count": 1,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'Berru'"
          },
          "metadata": {}
        }
      ],
      "id": "18f46235-1992-4631-8112-89bc24f97ccf"
    },
    {
      "cell_type": "code",
      "source": "age = 22\nage",
      "metadata": {
        "trusted": true
      },
      "execution_count": 2,
      "outputs": [
        {
          "execution_count": 2,
          "output_type": "execute_result",
          "data": {
            "text/plain": "22"
          },
          "metadata": {}
        }
      ],
      "id": "66b6a4a6-af89-4b94-9f87-59bdbbbe0368"
    },
    {
      "cell_type": "code",
      "source": "print(name)\nprint(age)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 3,
      "outputs": [
        {
          "name": "stdout",
          "text": "Berru\n22\n",
          "output_type": "stream"
        }
      ],
      "id": "27d5cb54-1508-4d5e-9621-c216527644b8"
    },
    {
      "cell_type": "code",
      "source": "print(type(name))\nprint(type(age))",
      "metadata": {
        "trusted": true
      },
      "execution_count": 4,
      "outputs": [
        {
          "name": "stdout",
          "text": "<class 'str'>\n<class 'int'>\n",
          "output_type": "stream"
        }
      ],
      "id": "a84b8060-d98f-413c-9107-8d03f746b41c"
    },
    {
      "cell_type": "code",
      "source": "name = 'Berru'\ntype(name)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 5,
      "outputs": [
        {
          "execution_count": 5,
          "output_type": "execute_result",
          "data": {
            "text/plain": "str"
          },
          "metadata": {}
        }
      ],
      "id": "4a141264-fea0-4899-962c-2e7129a2a228"
    },
    {
      "cell_type": "code",
      "source": "items = ['Apple', 1.49, 'Banana', 2.56, 'Berry', 3.45, 'Cherry', 2.03]\nprint(items, type(items))",
      "metadata": {
        "trusted": true
      },
      "execution_count": 6,
      "outputs": [
        {
          "name": "stdout",
          "text": "['Apple', 1.49, 'Banana', 2.56, 'Berry', 3.45, 'Cherry', 2.03] <class 'list'>\n",
          "output_type": "stream"
        }
      ],
      "id": "014a93ac-c471-40bd-a0a4-757aa00692eb"
    },
    {
      "cell_type": "code",
      "source": "print(items[6])\n\nprint(items[1:5])\n\nprint(items[3:])\n\nprint(items[:3])",
      "metadata": {
        "trusted": true
      },
      "execution_count": 7,
      "outputs": [
        {
          "name": "stdout",
          "text": "Cherry\n[1.49, 'Banana', 2.56, 'Berry']\n[2.56, 'Berry', 3.45, 'Cherry', 2.03]\n['Apple', 1.49, 'Banana']\n",
          "output_type": "stream"
        }
      ],
      "id": "09f70679-a89d-492c-9818-23fba2f964c6"
    },
    {
      "cell_type": "code",
      "source": "items[2] = 'Melon'\nprint(items)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 8,
      "outputs": [
        {
          "name": "stdout",
          "text": "['Apple', 1.49, 'Melon', 2.56, 'Berry', 3.45, 'Cherry', 2.03]\n",
          "output_type": "stream"
        }
      ],
      "id": "fa214684-04ed-4d5c-9545-8f0dc07936ab"
    },
    {
      "cell_type": "code",
      "source": "age = 22\nprint(age, type(age))",
      "metadata": {
        "trusted": true
      },
      "execution_count": 9,
      "outputs": [
        {
          "name": "stdout",
          "text": "22 <class 'int'>\n",
          "output_type": "stream"
        }
      ],
      "id": "c7dbedc6-034e-468d-a24d-6791dd3b11a7"
    },
    {
      "cell_type": "code",
      "source": "age = 22\nage += 0.5\nprint(age, type(age))",
      "metadata": {
        "trusted": true
      },
      "execution_count": 10,
      "outputs": [
        {
          "name": "stdout",
          "text": "22.5 <class 'float'>\n",
          "output_type": "stream"
        }
      ],
      "id": "1d56f5df-7dea-4d13-90a6-97072fdd2068"
    },
    {
      "cell_type": "code",
      "source": "age = '22'\nprint(type(age))",
      "metadata": {
        "trusted": true
      },
      "execution_count": 11,
      "outputs": [
        {
          "name": "stdout",
          "text": "<class 'str'>\n",
          "output_type": "stream"
        }
      ],
      "id": "dba32ff0-9cc5-4562-9666-ae581ccf1e21"
    },
    {
      "cell_type": "code",
      "source": "age = int(age)\nprint(age, type(age))",
      "metadata": {
        "trusted": true
      },
      "execution_count": 12,
      "outputs": [
        {
          "name": "stdout",
          "text": "22 <class 'int'>\n",
          "output_type": "stream"
        }
      ],
      "id": "ee3b2739-cf4b-44fd-84ef-c001b6ec18d6"
    }
  ]
}