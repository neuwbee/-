{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP69jLE3EtnVaItDtkeGsrF",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/neuwbee/-/blob/main/%ED%8C%8C%EC%9D%B4%EC%8D%AC_3%EC%A3%BC%EC%B0%A8_%EC%88%98%EC%97%85%EB%82%B4%EC%9A%A9.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0MFNk7fVa-AN",
        "outputId": "806a1ddf-a6c1-44f0-abcb-415c9d73ab49"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "list"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ],
      "source": [
        "a=[1,2,3,4,5]\n",
        "# [1,2,3.4.5]라는 배열을 A에 할당해라 - 해석\n",
        "\n",
        "type(a)\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(type(a))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "08IWRsgVeYNH",
        "outputId": "f89deecf-3d4a-42ac-fab9-749b5e2fa14d"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'list'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "type_a = type(a)\n"
      ],
      "metadata": {
        "id": "l3PcU1J4ejkT"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "type(type(a))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2-_d7iOYesCD",
        "outputId": "91e5356b-a1c2-4b9f-cac5-cdc229ae5840"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "type"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#리스트 안의 내용들 = 요소(element)"
      ],
      "metadata": {
        "id": "TcSpnWZxeyXa"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "a = [1,2,3,4,5]\n",
        "b = [1,2,3,4, 'streaser']\n",
        "a+b"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oV96uMOhfH3u",
        "outputId": "bcad0fe0-2d26-4b65-b265-240921c40bf0"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 2, 3, 4, 5, 1, 2, 3, 4, 'streaser']"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a-b"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 147
        },
        "id": "81L-kp8kfhGq",
        "outputId": "8e4bb23b-3053-4a3c-d7e8-d21c8ea6526d"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-8-5ae0619f8fe1>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0ma\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0mb\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a*b"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 147
        },
        "id": "D7m7MhzSfjxj",
        "outputId": "c7f86651-0da8-4bf0-f9a9-f3dbc20eb37a"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "can't multiply sequence by non-int of type 'list'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-9-8ce765dcfa30>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0ma\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mb\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m: can't multiply sequence by non-int of type 'list'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=[1,2,3,4]\n",
        "b=3\n",
        "a*b"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LL3PY_4WfvoB",
        "outputId": "3d30bde1-ce0c-4be4-f210-673331d5bded"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 리스트에서 요소의 개수를 알고 싶을때 len()를 사용해라\n"
      ],
      "metadata": {
        "id": "0naV72PAf1vK"
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "len(a*b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wqaouT5SgIDk",
        "outputId": "71ffccee-5679-4bc9-f606-3f0282ae0b08"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "12"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "test_text = 'python_programming'"
      ],
      "metadata": {
        "id": "dxPHqe-LgNsk"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 새 섹션"
      ],
      "metadata": {
        "id": "EAL0ulvcgggK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "len(test_text)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7iAdHbEhgiJA",
        "outputId": "72d95e91-acf4-437f-8672-84b246c0d8e5"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "18"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "letter_grades=['A', 'B', 'C', 'D']"
      ],
      "metadata": {
        "id": "CmQxGev8giWA"
      },
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "letter_grades.append('F')"
      ],
      "metadata": {
        "id": "_UFT3Xi9hiCY"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "letter_grades"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cRhLDO4Mhuzj",
        "outputId": "b9c5072c-3a54-4aa7-9b46-d2c3701ddd38"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['A', 'B', 'C', 'D', 'F']"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#append = 맨 뒤에 넣어라\n"
      ],
      "metadata": {
        "id": "ca1VivkNhzXD"
      },
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#요소를 내가 넣고 싶은 자리에 넣는 방법\n",
        "#insert() 사용하기"
      ],
      "metadata": {
        "id": "jioW7tMMh_Bj"
      },
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 모든 코딩에서 인덱스는 1이 아닌 0부터 시작\n",
        "# ex) ['a', 'b', 'c', 'd'] 일때 'a'는 0의 자리"
      ],
      "metadata": {
        "id": "8PtsIAsPiELX"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "letter_grades.insert(0, 'A+')"
      ],
      "metadata": {
        "id": "j6NHxwBiivqS"
      },
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(letter_grades)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Hi2BxJ5qi7HM",
        "outputId": "fe9eec55-c685-43d5-ebea-277429b97b7a"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['A+', 'A', 'B', 'C', 'D']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "'B' in letter_grades"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3nA2678Yi870",
        "outputId": "ab97bef1-873a-4332-e823-8487aa07c623"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "'E' in letter_grades"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uRiz8xX2jx_8",
        "outputId": "983bf18b-bf54-4dab-f537-f9e83a3b444a"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "'E' in 3"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 147
        },
        "id": "lA7CXEmakEDr",
        "outputId": "f552f792-a569-42dd-ef63-ade15866adf5"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "argument of type 'int' is not iterable",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-28-e27de1077613>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;34m'E'\u001b[0m \u001b[0;32min\u001b[0m \u001b[0;36m3\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m: argument of type 'int' is not iterable"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "empty_list = []"
      ],
      "metadata": {
        "id": "r96rVhYekHbL"
      },
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 요소가 없더라도 list이다\n"
      ],
      "metadata": {
        "id": "8LeGeZwfkWY8"
      },
      "execution_count": 30,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "'E' in empty_list"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-WF45z23keA8",
        "outputId": "7249d3e7-9d05-49f6-c19f-5128b427e9fe"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "letter_grades.index('D')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b0MdH5tYkl1M",
        "outputId": "90baef25-334b-4f38-a414-3e90b6ade1c9"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# pop과 remove의 차이 : pop은 index값을 줘야하고 remove는 요소를 주면 삭제한다"
      ],
      "metadata": {
        "id": "avLZamI-lBcG"
      },
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "letter_grades.pop(0)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "RVM_Tc9slzvn",
        "outputId": "0e74cf5f-0c6b-46e8-9219-c22cf43224b7"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'A+'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 35
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('letter_grades')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cT7adNs4l5Tc",
        "outputId": "a84c3744-313b-46e2-978f-308f4c854b9f"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "letter_grades\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(letter_grades)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RFPW2Ntul_lD",
        "outputId": "361cdc47-c8ef-4dac-e7d5-38077a7d785d"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['A', 'B', 'C', 'D']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "letter_grades.remove('D')"
      ],
      "metadata": {
        "id": "s_N-6hTtmCME"
      },
      "execution_count": 38,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(letter_grades)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1podYMd0mInj",
        "outputId": "9d2e1dc0-2ac6-41ee-e972-d1ad68e66695"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['A', 'B', 'C']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BJsEuvrxpmsm",
        "outputId": "87c151be-9651-4b6a-a620-88d562330373"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 2, 3, 4]"
            ]
          },
          "metadata": {},
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a.sort()"
      ],
      "metadata": {
        "id": "42y_xTGrppyE"
      },
      "execution_count": 43,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "a = [3,2,6,2,7,4]"
      ],
      "metadata": {
        "id": "fjN_IvMxpsqV"
      },
      "execution_count": 44,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "a.sort()"
      ],
      "metadata": {
        "id": "JHFjRFltp4Dt"
      },
      "execution_count": 45,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "a"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Xa-zGiiQp712",
        "outputId": "b635c73d-5835-4efa-b379-cabaef24a188"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[2, 2, 3, 4, 6, 7]"
            ]
          },
          "metadata": {},
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a.sort(reverse=True)"
      ],
      "metadata": {
        "id": "fYtBZ1z7p9jt"
      },
      "execution_count": 47,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "a"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e_Z9yAICqFJ9",
        "outputId": "9034cc9e-3be0-4aa4-939d-9753ebf05ff6"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[7, 6, 4, 3, 2, 2]"
            ]
          },
          "metadata": {},
          "execution_count": 48
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a.pop(5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZbVf_iGYqFu1",
        "outputId": "f701c6fc-56d9-43ea-9931-5acfc3ac7b62"
      },
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "metadata": {},
          "execution_count": 50
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0BOaiY4xqnnW",
        "outputId": "fc861a6e-2b9d-477f-dc7f-38b8c735ba19"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[7, 6, 4, 3, 2]"
            ]
          },
          "metadata": {},
          "execution_count": 51
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(a[-1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0kTr0qWKqrad",
        "outputId": "cac37445-b22a-4a08-ac46-3b120e3a8d1c"
      },
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(a[-2])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4B3lxd9xqyK2",
        "outputId": "687215b5-4977-4e83-966a-4f8ef55391cb"
      },
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(a[-6])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 147
        },
        "id": "91OSKD2vq1ik",
        "outputId": "16f3625f-1801-4c8e-f76d-3133d1d34655"
      },
      "execution_count": 54,
      "outputs": [
        {
          "output_type": "error",
          "ename": "IndexError",
          "evalue": "list index out of range",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-54-f790fd4f8aff>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m6\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mIndexError\u001b[0m: list index out of range"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(a[0])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X_YgD1veq40-",
        "outputId": "d4c8eb2d-28a7-4ba9-ed33-c76ec47c47a4"
      },
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 조건문 : if 다음에 조건절이 오는 구문으로 참 거짓의 boolean 형태로 결과가 출력된다. (비교 연산자)"
      ],
      "metadata": {
        "id": "msyZcj2wv6d-"
      },
      "execution_count": 87,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "x= 180\n",
        "y= 70\n",
        "if (x-100)*0.9 > y:\n",
        "  print(\"저체중\")\n",
        "elif(x-100)*0.9 == y:\n",
        "  print(\"정상체중\")\n",
        "else:\n",
        "  print(\"과체중\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "71klaXRhw9Ke",
        "outputId": "dab70b88-24c6-4503-a423-b0503a0ea40d"
      },
      "execution_count": 89,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "저체중\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = 100\n",
        "if (0<x<57):\n",
        "  print(\"플라이\")\n",
        "elif (57 < x < 61.2):\n",
        "  print(\"밴텀\")\n",
        "elif(61.2 < x < 65.8):\n",
        "  print(\"페더\")\n",
        "elif(65.8 < x < 70.3):\n",
        "  print(\"라이트\")\n",
        "elif(70.3 < x < 77.1):\n",
        "  print(\"웰터\")\n",
        "elif(77.1 < x < 83.9):\n",
        "  print(\"미들\")\n",
        "elif(83.9 < x < 93):\n",
        "  print(\"라이트_헤비\")\n",
        "elif(93 < x < 120.2):\n",
        "  print(\"헤비\")\n",
        "else:\n",
        "  print(\"규격 외\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nOHZwfmHyY8k",
        "outputId": "45c687a0-1b9a-424c-beb5-47d5a51b7cd4"
      },
      "execution_count": 103,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "헤비\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = 1 to 100"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 110
        },
        "id": "0lvdFucy0Gbf",
        "outputId": "9d8d4d11-d999-4e52-f3f6-6c4c0b904f03"
      },
      "execution_count": 96,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax (<ipython-input-96-96b80eb89e6f>, line 1)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-96-96b80eb89e6f>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    x = 1 to 100\u001b[0m\n\u001b[0m          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3obbxIYZ06we",
        "outputId": "49cb8439-043a-4b30-ac99-0cdc89bcc126"
      },
      "execution_count": 100,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "틀림\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "diH5HNDZ18iP"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}