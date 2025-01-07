{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2cd526c2-5cad-4130-88f4-db3ae90ffb39",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 4, 9, 78}\n",
      "<class 'set'>\n"
     ]
    }
   ],
   "source": [
    "s1 = {1,2,2,3,3,4,78,9}\n",
    "print(s1)\n",
    "print(type(s1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fd6f662d-9ab5-4a28-b82b-474934b03a60",
   "metadata": {},
   "outputs": [],
   "source": [
    "lst1=[1,8,9,0,10,20,78,8,8,8]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "fb4de23a-d494-4e4b-a8aa-78ea7ad8dc7a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0, 1, 8, 9, 10, 78, 20}\n",
      "<class 'set'>\n"
     ]
    }
   ],
   "source": [
    "s2=set(lst1)\n",
    "print(s2)\n",
    "print(type(s2))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "2d238ab1-af09-478f-a4e8-918d477d6825",
   "metadata": {},
   "outputs": [],
   "source": [
    "s1={1,2,3,4}\n",
    "s2={3,4,5,6}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "400ae09c-27f5-459f-a704-b43c629434a3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 5, 6}"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "s1 | s2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e88d783c-2fe1-49df-a159-dbab6b07fb3e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 5, 6}"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1.union(s2)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "59d8db0d-4872-412c-8a99-d8b912499d13",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Intersection using & operator\n",
    "s1={1,2,3,4}\n",
    "s2={3,4,5,6}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "2037b938-cfa0-4a18-a19f-f8b897225b97",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{3, 4}"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1 & s2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "036a407b-6214-4120-8cd9-8d9259181f9b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#difference of two sets\n",
    "s1={2,3,5,6,7}\n",
    "s2={5,6,7}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "ebc3e8a5-3fcf-4ceb-a80d-849c6b8eba2e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{2, 3}"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1 - s2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "bdda8102-6884-4414-96ae-c42569629937",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Symmetric difference\n",
    "s1={1,2,3,4,5}\n",
    "s2={4,5,6,7,8}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "b77c2657-92fb-4bf1-8cea-ff882f9c0b84",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 6, 7, 8}"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1.symmetric_difference(s2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "f326cbe9-9884-4119-ba05-772a102dcd1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "s1={1,2,3,4,5}\n",
    "s2={1,2,3}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "96394ef8-42f8-473c-bcb5-14499ac384c6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2.issubset(s1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "13125ca3-12eb-42b7-8083-43a931624ec2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2.issuperset(s1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "9447a388-cf67-4cbc-a10e-a55c318b7e6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#STRINGs\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "f55ea09c-6467-464b-9de0-d6c13a48f460",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to aiml class\n",
      "We started with python\n",
      "This is an awesome class\n"
     ]
    }
   ],
   "source": [
    "str1=\"Welcome to aiml class\"\n",
    "print(str1)\n",
    "str2='We started with python'\n",
    "print(str2)\n",
    "str3='''This is an awesome class'''\n",
    "print(str3)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "64ed337f-fb5a-4a00-abd9-9c186868803a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n",
      "<class 'str'>\n",
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "print(type (str1))\n",
    "print(type (str2))\n",
    "print(type (str3))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "b2de9c6f-645e-46d9-8ad9-a37181d22d9a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to aiml class\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'me to'"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(str1)\n",
    "str1[5:10]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "768d2205-aefe-4f71-b461-a8b2d6a3f8b8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'The product is awesomeGreat Service'"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reviews=[\"The product is awesome\", \"Great Service\"]\n",
    "joined_string=''.join(reviews)\n",
    "joined_string\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "c58092c4-4485-4718-973a-2d44177ab788",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'    Hello, How are you?    '"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Use of strip() method\n",
    "str5=\"    Hello, How are you?    \"\n",
    "str5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "5db593c0-144b-4346-b467-449f85934387",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello, How are you?'"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " str5.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "8e19462a-7697-41f2-b36a-9bd1d768bc93",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello, How are you?'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str5.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "c33f8e7a-1802-46d8-98ce-b7730b46e4e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello, how are you?'"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str5=\"Hello, How are you?\"\n",
    "str5.lower()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "9135327f-44e6-4f53-95b5-7ef1c2b233d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'    HELLO, HOW ARE YOU?    '"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str5.upper()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3393ed7-f061-4b0b-a45e-ffeff054730b",
   "metadata": {},
   "outputs": [],
   "source": [
    "      \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "53da0265-3ed3-43ac-bfee-18f20bd579d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "d1={\"Ram\": 180, \"Shyam\":170,\"Ramya\":176}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c69ccb65-7870-401c-a995-aeb01f9aedc1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "7d439238-4994-4fb3-ab7e-bd083191e5e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ram 180\n",
      "Shyam 170\n",
      "Ramya 176\n"
     ]
    }
   ],
   "source": [
    "for k,v in d1.items():\n",
    "    print(k,v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c33df77-7eef-41c7-bd3c-071413feef92",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
