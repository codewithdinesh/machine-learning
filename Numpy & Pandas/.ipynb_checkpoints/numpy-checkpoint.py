{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "15bbbc10-82f9-47f8-b09d-3b093cda4b19",
   "metadata": {},
   "source": [
    "## This is My first Jupyter Notebook"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "62a7f9a0-b013-42ce-b114-8b4f128a450c",
   "metadata": {},
   "source": [
    "**Lets Learn Numpy**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e8573018-212b-4ecf-9081-3a2d80f738de",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f1470e62-9445-4830-b751-5eba87e9541e",
   "metadata": {},
   "source": [
    "**One D Array**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "5c45f992-73a9-4178-8d3e-ba63698e400f",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.array(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "a71814c0-073a-45bb-a8d2-8c57b16781f3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(4)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9f2b7cb9-d8bf-45a1-99b9-3d8a808e2103",
   "metadata": {},
   "source": [
    "**1 D Array**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "70f4387b-c14c-4e04-9f9c-44a6fcd01167",
   "metadata": {},
   "outputs": [],
   "source": [
    "myarray = np.array([5,61,12,24])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e0a40c9a-5e99-4ae5-9f44-38321baf18aa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 5, 61, 12, 24])"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myarray"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "127396bc-da47-431b-90f5-deea7ad9bff9",
   "metadata": {},
   "source": [
    "##### **2 Dimension Array**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "e6848452-e797-44b9-a5df-a6d27e78ac53",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr  = np.array([[2,3,4,5],[7,2,1,3]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "43a62e13-c202-4e5c-97b2-51daa93fd112",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[2, 3, 4, 5],\n",
       "       [7, 2, 1, 3]])"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7561d8b1-fda7-40c9-befb-f06e6c873b2a",
   "metadata": {},
   "source": [
    "**n-D array**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "1bb4edd1-8bb0-4306-b426-cc44611371b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.array([[[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[10, 11, 12]]])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "a3ab941d-c36a-4efd-b4ca-a0b4834c4a56",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[ 1,  2,  3],\n",
       "        [ 4,  5,  6]],\n",
       "\n",
       "       [[ 7,  8,  9],\n",
       "        [10, 11, 12]]])"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "89607cbb-a91a-4360-a699-3a7e6e271cb6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "print(arr.ndim)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "904b1914-9d92-4526-9a0d-5e109ed96a2d",
   "metadata": {},
   "source": [
    "**Array types or size**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a7342d5e-32a3-4eae-9a46-bc20df33681a",
   "metadata": {},
   "outputs": [],
   "source": [
    "newarr=np.array([5,61,234,55,23], np.int64)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "16f9bd43-9c00-4874-bc71-23de1c57484e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  5,  61, 234,  55,  23], dtype=int64)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "newarr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "cccce40d-2bc2-45de-b694-638fd31ab8dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr=np.array([5,61,234,55,23], np.int32)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3a97db6c-5f3d-499a-b10e-57f8c0cd80cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('int64')"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "newarr.dtype"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e96bb673-a06c-461e-98d8-87919050bc9d",
   "metadata": {},
   "source": [
    "**Properties**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c002793a-3880-4bff-b91f-dc65abbab2ae",
   "metadata": {},
   "source": [
    "***Create N dimensional Array***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "73e76c07-2e8b-4e36-80e9-600d25c50309",
   "metadata": {},
   "outputs": [],
   "source": [
    "ndarray = np.array([1,2,4,6],ndmin=5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "885eda29-6f83-4663-9688-71c45b9d8b68",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[[[1, 2, 4, 6]]]]])"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ndarray"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8d7469f1-82a6-494e-b8cd-713f5af28bce",
   "metadata": {},
   "source": [
    "***Data Access From Array***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "14c08713-d7de-49c1-b2b4-09777e97dfbf",
   "metadata": {},
   "outputs": [],
   "source": [
    "temp = np.array([[5,8,2,6,7]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3b0248b3-9ced-46a3-a2aa-9bc4776400e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[5 8 2 6 7]]\n"
     ]
    }
   ],
   "source": [
    "print(temp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "acf46d63-861b-4d87-8b36-3462a6a8610c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "print(temp[0][2])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8286128c-352a-4db9-b248-463b44d30bbb",
   "metadata": {},
   "source": [
    "***Accessing n-D array***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "ed0f893d-57b5-44ee-a5da-e8a753626072",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Element at 0[1[2]] =  6\n",
      "Dimension of array =  3\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])\n",
    "\n",
    "print(\"Element at 0[1[2]] = \",arr[0, 1, 2])\n",
    "\n",
    "print(\"Dimension of array = \",arr.ndim)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a31880af-3616-48f2-b6a7-da929275e290",
   "metadata": {},
   "source": [
    "***Negative Accessing***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "b40c7110-57b1-4507-a8f2-a7f16770fe31",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array =  [9 8 6 3]\n",
      "Last Element [-1] =  3\n"
     ]
    }
   ],
   "source": [
    "arr_simple = np.array([9,8,6,3])\n",
    "\n",
    "print(\"Array = \",arr_simple)\n",
    "\n",
    "print(\"Last Element [-1] = \",arr_simple[-1])\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "5e5be2eb-a156-4d79-8074-0cfdaeeeb39a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array Elements:  [[1 2 3 4]\n",
      " [5 6 7 8]]\n",
      "Element at [1,-1] =  8\n"
     ]
    }
   ],
   "source": [
    "arr_negative_access = np.array([[1,2,3,4],[5,6,7,8]])\n",
    "\n",
    "\n",
    "print(\"Array Elements: \", arr_negative_access)\n",
    "\n",
    "print(\"Element at [1,-1] = \", arr_negative_access[1,-1])\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7f520ff6-3df5-453a-941f-dbe5246a7180",
   "metadata": {},
   "source": [
    "***Array Slicing***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "70491796-7333-477f-ac5f-6d70e306379c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array :  [1 4 6 7 8]\n",
      "Array Element from 2nd to 5th [6 7 8]\n"
     ]
    }
   ],
   "source": [
    "temp = np.array([1,4,6,7,8])\n",
    "\n",
    "print(\"Array : \", temp)\n",
    "\n",
    "print(\"Array Element from 2nd to 5th\", temp[2:5])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c258f6bc-d529-4827-9012-64b17f7933a6",
   "metadata": {},
   "source": [
    "***Negative Array Slicing***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "83fc9ca6-3ce1-4fd1-a0dd-78e3d4d88faf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array Elements upto -1 to :  [1 4 6 7]\n",
      "Array Elements from -4 to :  [4 6 7 8]\n"
     ]
    }
   ],
   "source": [
    "print(\"Array Elements upto -1 to : \",temp[:-1])\n",
    "print(\"Array Elements from -4 to : \",temp[-4: ])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "701e670f-ece3-41ce-a72f-45a82c4a26fb",
   "metadata": {},
   "source": [
    "***Array Slicing With Steps***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "0950ec0c-05cc-4a49-b6b1-caf62a8985bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array:  [1 4 6 7 8]\n",
      "Array Elements from 1 to 5 with step 2:  [4 7]\n"
     ]
    }
   ],
   "source": [
    "print(\"Array: \",temp)\n",
    "print(\"Array Elements from 1 to 5 with step 2: \",temp[1:5:2])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8911a5a4-d5c1-4b09-a240-5c58852a9ab4",
   "metadata": {},
   "source": [
    "***Slicing 2D array***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "60aa249d-517c-401b-a4fd-582fc0c9edfa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array =  [[ 1  2  3  4  5]\n",
      " [ 6  7  8  9 10]]\n",
      "Array Elements from 2 to 5 at 2nd inner array:  [ 8  9 10]\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])\n",
    "\n",
    "print(\"Array = \", arr)\n",
    "\n",
    "print(\"Array Elements from 2 to 5 at 2nd inner array: \",arr[1,2:5])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee939299-16e9-445d-9689-e314bf602f3e",
   "metadata": {},
   "source": [
    "***Data Types in Numpy***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "b811ad75-76d5-418f-9c4a-2973e9e2fdc8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array =  [1 2 3 4]\n",
      "Array Data type :  int32\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([1, 2, 3,4])\n",
    "\n",
    "print(\"Array = \", arr)\n",
    "\n",
    "print(\"Array Data type : \",arr.dtype)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "6cfbfbae-d0e0-4b52-9053-1f547559848f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array =  ['dinesh' 'omkar' 'tanmay']\n",
      "Array data type:  <U6\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([\"dinesh\",\"omkar\",\"tanmay\"])\n",
    "\n",
    "print(\"Array = \", arr)\n",
    "\n",
    "print(\"Array data type: \" ,arr.dtype)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "114222f5-fb2f-4beb-8429-b578414eacc3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array =  ['dinesh' 'omkar' 'tanmay']\n",
      "Array data type:  <U6\n"
     ]
    }
   ],
   "source": [
    "arr = np.array(['dinesh','omkar','tanmay'])\n",
    "\n",
    "print(\"Array = \", arr)\n",
    "\n",
    "print(\"Array data type: \" ,arr.dtype)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5b32b648-ac37-4c36-a4b9-1ea6615beb0a",
   "metadata": {},
   "source": [
    "***Assigning Data Types to array***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "71cd28aa-b114-4236-843a-ba59d28d3c55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array =  [b'dinesh' b'omkar' b'tanmay']\n",
      "Array data type:  |S6\n"
     ]
    }
   ],
   "source": [
    "arr = np.array(['dinesh','omkar','tanmay'],dtype=\"S\")\n",
    "\n",
    "print(\"Array = \", arr)\n",
    "\n",
    "print(\"Array data type: \" ,arr.dtype)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f33b9401-005a-4196-af1d-e4026f8e33ef",
   "metadata": {},
   "source": [
    "***Converting Data Types of Array***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "85307f80-e340-4eae-bf24-4d444fc6bea6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array :  [1.1 1.5 2.5 6.1]\n",
      "Array After Conversion (float to int):  [1 1 2 6]\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([1.1, 1.5, 2.5, 6.1])\n",
    "\n",
    "print(\"Array : \", arr)\n",
    "\n",
    "newarr = arr.astype('i')\n",
    "\n",
    "print(\"Array After Conversion (float to int): \", newarr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "45f920aa-e602-44c8-a35f-5a5da99250fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ True False  True]\n",
      "bool\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([1, 0, 3])\n",
    "\n",
    "newarr = arr.astype(bool)\n",
    "\n",
    "print(newarr)\n",
    "print(newarr.dtype)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4ba28b25-e9a7-4eb4-ae76-3671d8d6c6f2",
   "metadata": {},
   "source": [
    "***NumPy Array Copy vs View*** <br>\n",
    "*Copy create new array: can not change from original updation*<br>\n",
    "*View() create copy of array : if we change original its new array also changes*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "45f7e06f-86c5-45ec-a09b-7b2abeb1d97b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Array:  [42  2  3  4  5]\n",
      "New Array:  [1 2 3 4 5]\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([1, 2, 3, 4, 5])\n",
    "x = arr.copy()\n",
    "arr[0] = 42\n",
    "\n",
    "print(\"Original Array: \",arr)\n",
    "print(\"New Array: \", x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "24953e1c-caf8-4c33-875d-4d420b301479",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Array:  [42  2  3  4  5]\n",
      "New Array:  [42  2  3  4  5]\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([1, 2, 3, 4, 5])\n",
    "x = arr.view()\n",
    "arr[0] = 42\n",
    "\n",
    "print(\"Original Array: \",arr)\n",
    "print(\"New Array: \", x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "499a0533-3e96-4e1c-a386-db863ec39fb2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Base of copied original: None\n",
      "Base of view original: [1 2 3 4 5]\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([1, 2, 3, 4, 5])\n",
    "\n",
    "x = arr.copy()\n",
    "y = arr.view()\n",
    "\n",
    "print(\"Base of copied original:\", x.base)\n",
    "print(\"Base of view original:\" , y.base)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3f5bafd-b532-469c-81b9-e59f9eecbe6b",
   "metadata": {},
   "source": [
    "**NumPy Array Shape**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "14a34186-bba6-4868-b28b-368011d65ed5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array =  [[ 1  2  3  4  5]\n",
      " [ 6  7  8  9 10]]\n",
      "Shape of array (Dimension): (2, 5)\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])\n",
    "\n",
    "print(\"Array = \", arr)\n",
    "\n",
    "print(\"Shape of array (Dimension):\",arr.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "c644ee68-d1ab-4156-9a24-ffcc574604ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array:  [[[[[1 2 3 4]]]]]\n",
      "shape of array : (1, 1, 1, 1, 4)\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([1, 2, 3, 4], ndmin=5)\n",
    "\n",
    "print(\"Array: \",arr)\n",
    "print('shape of array :', arr.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4a8e11ab-1b82-4aa1-91a9-06ec235bd92f",
   "metadata": {},
   "source": [
    "***Reshape Array***"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b6d6deda-5ee9-4ced-9411-7f396f8947cb",
   "metadata": {},
   "source": [
    "*1D to 2D*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "3a25c886-bb66-4567-a638-3b02fb970554",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Array:  [ 1  2  3  4  5  6  7  8  9 10 11 12]\n",
      "Reshaped Array:  [[ 1  2  3]\n",
      " [ 4  5  6]\n",
      " [ 7  8  9]\n",
      " [10 11 12]]\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])\n",
    "\n",
    "newarr = arr.reshape(4, 3)\n",
    "\n",
    "print(\"Original Array: \",arr)\n",
    "print(\"Reshaped Array: \",newarr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "5bbbc7fc-7c3d-43a1-992a-2f2d5efcde1c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Array:  [ 1  2  3  4  5  6  7  8  9 10 11 12]\n",
      "Reshaped Array:  [[[ 1  2]\n",
      "  [ 3  4]\n",
      "  [ 5  6]]\n",
      "\n",
      " [[ 7  8]\n",
      "  [ 9 10]\n",
      "  [11 12]]]\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])\n",
    "\n",
    "newarr = arr.reshape(2,3,2)\n",
    "\n",
    "print(\"Original Array: \",arr)\n",
    "print(\"Reshaped Array: \",newarr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5fec815-60c4-4790-bd1d-9732ace6f10d",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
