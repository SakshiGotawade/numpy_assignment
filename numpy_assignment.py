{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7ae4a8c1-83c9-4917-9050-4979ea03c94d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: numpy in c:\\users\\gigabyte\\anaconda3\\lib\\site-packages (1.26.4)Note: you may need to restart the kernel to use updated packages.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "pip install numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "22cdb534-f09a-4dfc-a617-22055e24e4c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9b753995-1cd0-4c19-902a-c61466abbdc0",
   "metadata": {},
   "source": [
    "# 1 Creating a 1D array from 1 to 20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a29644c3-bc3c-4a6e-87a3-ee6ec1ca316c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1D Array: [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]\n"
     ]
    }
   ],
   "source": [
    "arr = np.arange (1,20)\n",
    "print(\"1D Array:\", arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2de62861-b4f0-4f09-83cd-2bbb402e8cb2",
   "metadata": {},
   "source": [
    " # 1A) Calculate the sum, mean, median, and standard deviation of the elements in the array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "2c8cb751-f05b-4827-943a-275877b5ede4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sum: 190\n",
      "mean: 10.0\n",
      "median: 10.0\n",
      "Standard Deviation: 5.477225575051661\n"
     ]
    }
   ],
   "source": [
    "print(\"sum:\", np.sum(arr))\n",
    "print(\"mean:\", np.mean(arr))\n",
    "print(\"median:\", np.median(arr))\n",
    "print(\"Standard Deviation:\", np.std(arr))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d53b7bfb-c326-4fcb-9491-aa96e60f34d3",
   "metadata": {},
   "source": [
    "# 1B) Indices of elements greater than 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "d1a035a9-cc79-40b7-9496-bb74cfddb115",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Indices of elements greater than 10: (array([10, 11, 12, 13, 14, 15, 16, 17, 18], dtype=int64),)\n"
     ]
    }
   ],
   "source": [
    "indices_gt_10 = np.where(arr > 10)\n",
    "print(\"Indices of elements greater than 10:\", indices_gt_10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f4e7ee9-6e7a-44cd-9677-cc92c402683d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "1812cd84-1abf-4b40-b4a4-078a7c8cc8e8",
   "metadata": {},
   "source": [
    "# 2 Creating a 2D NumPy array of shape 4 X 4 with numbers ranging from 1 to 16"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "779e24fc-85b0-49bb-b5a0-9cd07a04a8fe",
   "metadata": {},
   "source": [
    "# 2A) Printing array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c8caa7f9-592c-4abf-9ecf-0af3d36851d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3  4]\n",
      " [ 5  6  7  8]\n",
      " [ 9 10 11 12]\n",
      " [13 14 15 16]]\n"
     ]
    }
   ],
   "source": [
    "array_2d = np.arange(1, 17).reshape(4, 4)\n",
    "print(array_2d)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f280a235-9719-4cd7-b0d8-b14a0a6bfc8c",
   "metadata": {},
   "source": [
    "# 2 B) Transpose of the array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "0589dc97-f7ba-455a-8ce8-333d7a96be23",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  5  9 13]\n",
      " [ 2  6 10 14]\n",
      " [ 3  7 11 15]\n",
      " [ 4  8 12 16]]\n"
     ]
    }
   ],
   "source": [
    "transpose_array = array_2d.T\n",
    "print(transpose_array)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3f365896-f3b0-4865-8121-6e82bb82e358",
   "metadata": {},
   "source": [
    "# 2 C) Calculation of row-wise and column-wise sums of the array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "0001d4db-f32d-4b98-ae12-9f4ceec67a6a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10 26 42 58]\n",
      "[28 32 36 40]\n"
     ]
    }
   ],
   "source": [
    "row_sum = np.sum(array_2d, axis=1)\n",
    "col_sum = np.sum(array_2d, axis=0)\n",
    "\n",
    "print(row_sum)\n",
    "print(col_sum)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7b4c19e6-d797-4a33-9d89-b1ddc436ed5a",
   "metadata": {},
   "source": [
    "# 3. Creating two 3 X 3 arrays filled with random integers between 1 and 20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "4de6de49-ecf0-4212-aedd-9ce225ba3e55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 8  3 13]\n",
      " [11  3 18]\n",
      " [10 17 19]]\n",
      "[[ 8  7 15]\n",
      " [10 15 19]\n",
      " [ 8 18 19]]\n"
     ]
    }
   ],
   "source": [
    "array1 = np.random.randint(1, 21, size=(3, 3))\n",
    "array2 = np.random.randint(1, 21, size=(3, 3))\n",
    "print(array1)\n",
    "print(array2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "34f2755d-e9a3-4ff3-871e-332d9a5d33c4",
   "metadata": {},
   "source": [
    "# 3 A) Element-wise operations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "99afe3cb-0645-4fdf-9049-f3b88149d03b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[16 10 28]\n",
      " [21 18 37]\n",
      " [18 35 38]]\n",
      "[[  0  -4  -2]\n",
      " [  1 -12  -1]\n",
      " [  2  -1   0]]\n",
      "[[ 64  21 195]\n",
      " [110  45 342]\n",
      " [ 80 306 361]]\n"
     ]
    }
   ],
   "source": [
    "addition = array1 + array2\n",
    "subtraction = array1 - array2\n",
    "multiplication = array1 * array2\n",
    "\n",
    "print(addition)\n",
    "print(subtraction)\n",
    "print(multiplication)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "074a560c-25d6-4940-bca1-e17c12bdd397",
   "metadata": {},
   "source": [
    "# 3 B) Computing the dot product of the two arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "47d273be-68b1-492e-97a9-a5601cf0eb04",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[198 335 424]\n",
      " [262 446 564]\n",
      " [402 667 834]]\n"
     ]
    }
   ],
   "source": [
    "dot_product = np.dot(array1, array2)\n",
    "print(dot_product)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6b11f288-14b1-4ef8-8d9c-6e035a2cf5a3",
   "metadata": {},
   "source": [
    "# 4. Reshaping 1D array of size 12 into a 3 X 4 2D array and slice the first two rows and last two columns\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "4dd70d6d-bd16-4068-af27-af5d11bc5217",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 1  2  3  4  5  6  7  8  9 10 11 12]\n"
     ]
    }
   ],
   "source": [
    "arr_1d = np.arange(1, 13)\n",
    "print(arr_1d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "0755dc24-79dc-4360-ac2d-4407532ece67",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3  4]\n",
      " [ 5  6  7  8]\n",
      " [ 9 10 11 12]]\n"
     ]
    }
   ],
   "source": [
    "reshaped_array = arr_1d.reshape(3, 4)\n",
    "print(reshaped_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "0667c9c4-537a-403c-9bc3-4bc0265219f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[3 4]\n",
      " [7 8]]\n"
     ]
    }
   ],
   "source": [
    "sliced_array = reshaped_array[:2, -2:]\n",
    "print(sliced_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e77febba-e7c1-4022-b198-4e7df594624b",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
