{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ed88e7d6-84ac-4461-8272-fc59748664dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "numbers = [1, 2, 3, 4, 5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "80b5e3e8-8f62-4748-b492-91daea92a571",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "'in' expected after for-loop variables (3252818966.py, line 2)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mresult = [x**2 for x inn numbers if x % 2 != 0]\u001b[39m\n                         ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m 'in' expected after for-loop variables\n"
     ]
    }
   ],
   "source": [
    "numbers = [1, 2, 3, 4, 5]\n",
    "result = [x**2 for x inn numbers if x % 2 != 0]\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "66bdc0b3-e5ae-440b-8c1a-e80306ab7b1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 9, 25]\n"
     ]
    }
   ],
   "source": [
    "numbers = [1, 2, 3, 4, 5]\n",
    "result = [x**2 for x in numbers if x % 2 != 0]\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d90c3ba7-9e49-4abb-98b7-8fb7b6f8ee36",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1256818751.py, line 2)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[4]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mresult = [x**3 for x in numbers if x % 2 = 0]\u001b[39m\n                                             ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "result = [x**3 for x in numbers if x % 2 = 0]\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1a15e300-ee4d-4546-bfcf-cb849bfe65fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[8, 64, 216, 512, 1000]\n"
     ]
    }
   ],
   "source": [
    "numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "result = [x**3 for x in numbers if x % 2 == 0]\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4fcdf959-eacb-4416-98ed-4cfdad96ef5d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Salom, Salom!\n"
     ]
    }
   ],
   "source": [
    "def salomlash(ism):\n",
    "    return f\"Salom, {ism}!\"\n",
    "\n",
    "print(salomlash(\"Salom\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ef2ee7b4-6f16-425d-89c1-f5e5fd223110",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Salom, Ali!\n"
     ]
    }
   ],
   "source": [
    "def salomlash(ism):\n",
    "    return f\"Salom, {ism}!\"\n",
    "\n",
    "print(salomlash(\"Ali\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e5ae4119-b5a3-4902-acaf-455b52543d89",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Katta odam\n",
      "Voyaga yetmagan\n"
     ]
    }
   ],
   "source": [
    "def yosh_tekshir(yosh):\n",
    "    if yosh >= 18:\n",
    "        return \"Katta odam\"\n",
    "    else:\n",
    "        return \"Voyaga yetmagan\"\n",
    "\n",
    "print(yosh_tekshir(20))\n",
    "print(yosh_tekshir(15))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "bda100eb-56a0-4e7b-9e5e-566c5ba00a18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n"
     ]
    }
   ],
   "source": [
    "def eng_katta(sonlar):\n",
    "    eng_kata = sonlar[0]\n",
    "    for son in sonlar:\n",
    "        if son > eng_kata:\n",
    "            eng_kata = son\n",
    "    return eng_kata\n",
    "\n",
    "print(eng_katta([3, 7, 2, 9, 1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0b6c326a-2e38-4620-9602-4b20de5db5ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "30\n",
      "25\n"
     ]
    }
   ],
   "source": [
    "def yigindisi(*sonlar):\n",
    "    natija = 0\n",
    "    for son in sonlar:\n",
    "        natija += son\n",
    "    return natija\n",
    "\n",
    "print(yigindisi(1, 2, 3))\n",
    "print(yigindisi(10, 20))\n",
    "print(yigindisi(5, 5, 5, 5, 5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "587937c7-74ce-4aca-8425-c2dab7839da2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "30\n",
      "25\n"
     ]
    }
   ],
   "source": [
    "def yigindisi(*sonlar):\n",
    "    natija = 0\n",
    "    for son in sonlar:\n",
    "        natija += son\n",
    "    return natija\n",
    "\n",
    "print(yigindisi(1, 2, 3))\n",
    "print(yigindisi(10, 20))\n",
    "print(yigindisi(5, 5, 5, 5, 5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "687f2d71-846d-49f9-a638-0413213a986f",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "yigindisi() takes 1 positional argument but 3 were given",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[11]\u001b[39m\u001b[32m, line 7\u001b[39m\n\u001b[32m      3\u001b[39m     \u001b[38;5;28;01mfor\u001b[39;00m son \u001b[38;5;28;01min\u001b[39;00m sonlar:\n\u001b[32m      4\u001b[39m         natija += son\n\u001b[32m      5\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m natija\n\u001b[32m      6\u001b[39m \n\u001b[32m----> \u001b[39m\u001b[32m7\u001b[39m print(yigindisi(\u001b[32m1\u001b[39m, \u001b[32m2\u001b[39m, \u001b[32m3\u001b[39m))\n\u001b[32m      8\u001b[39m print(yigindisi(\u001b[32m10\u001b[39m, \u001b[32m20\u001b[39m))\n\u001b[32m      9\u001b[39m print(yigindisi(\u001b[32m5\u001b[39m, \u001b[32m5\u001b[39m, \u001b[32m5\u001b[39m, \u001b[32m5\u001b[39m, \u001b[32m5\u001b[39m))\n",
      "\u001b[31mTypeError\u001b[39m: yigindisi() takes 1 positional argument but 3 were given"
     ]
    }
   ],
   "source": [
    "def yigindisi(sonlar):\n",
    "    natija = 0\n",
    "    for son in sonlar:\n",
    "        natija += son\n",
    "    return natija\n",
    "\n",
    "print(yigindisi(1, 2, 3))\n",
    "print(yigindisi(10, 20))\n",
    "print(yigindisi(5, 5, 5, 5, 5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "c305f0b1-fa1b-4f01-93bf-f54ff280786d",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'int' object is not iterable",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[12]\u001b[39m\u001b[32m, line 6\u001b[39m\n\u001b[32m      2\u001b[39m     natija = \u001b[32m0\u001b[39m\n\u001b[32m      3\u001b[39m     \u001b[38;5;28;01mfor\u001b[39;00m son \u001b[38;5;28;01min\u001b[39;00m sonlar:\n\u001b[32m      4\u001b[39m         natija += son\n\u001b[32m      5\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m natija\n\u001b[32m----> \u001b[39m\u001b[32m6\u001b[39m print(yigindisi(\u001b[32m1\u001b[39m))\n\u001b[32m      7\u001b[39m print(yigindisi(\u001b[32m3\u001b[39m))\n\u001b[32m      8\u001b[39m print(yigindisi(\u001b[32m6\u001b[39m))\n",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[12]\u001b[39m\u001b[32m, line 3\u001b[39m, in \u001b[36myigindisi\u001b[39m\u001b[34m(sonlar)\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m yigindisi (sonlar):\n\u001b[32m      2\u001b[39m     natija = \u001b[32m0\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m3\u001b[39m     \u001b[38;5;28;01mfor\u001b[39;00m son \u001b[38;5;28;01min\u001b[39;00m sonlar:\n\u001b[32m      4\u001b[39m         natija += son\n\u001b[32m      5\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m natija\n",
      "\u001b[31mTypeError\u001b[39m: 'int' object is not iterable"
     ]
    }
   ],
   "source": [
    "def yigindisi (sonlar):\n",
    "    natija = 0 \n",
    "    for son in sonlar:\n",
    "        natija += son\n",
    "    return natija\n",
    "print(yigindisi(1))\n",
    "print(yigindisi(3))\n",
    "print(yigindisi(6))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a3fab6be-90a1-4162-9dfa-0408e0117cf9",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'function' object is not iterable",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[13]\u001b[39m\u001b[32m, line 7\u001b[39m\n\u001b[32m      3\u001b[39m     \u001b[38;5;28;01mfor\u001b[39;00m son \u001b[38;5;28;01min\u001b[39;00m juft_yigindi:\n\u001b[32m      4\u001b[39m         \u001b[38;5;28;01mif\u001b[39;00m son % \u001b[32m2\u001b[39m == \u001b[32m0\u001b[39m:\n\u001b[32m      5\u001b[39m             natija += son\n\u001b[32m      6\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m yigindi\n\u001b[32m----> \u001b[39m\u001b[32m7\u001b[39m print(juft_yigindi(\u001b[32m1\u001b[39m, \u001b[32m2\u001b[39m, \u001b[32m3\u001b[39m, \u001b[32m4\u001b[39m, \u001b[32m5\u001b[39m, \u001b[32m6\u001b[39m))\n",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[13]\u001b[39m\u001b[32m, line 3\u001b[39m, in \u001b[36mjuft_yigindi\u001b[39m\u001b[34m(*sonlar)\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m juft_yigindi(*sonlar):\n\u001b[32m      2\u001b[39m     natija = \u001b[32m0\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m3\u001b[39m     \u001b[38;5;28;01mfor\u001b[39;00m son \u001b[38;5;28;01min\u001b[39;00m juft_yigindi:\n\u001b[32m      4\u001b[39m         \u001b[38;5;28;01mif\u001b[39;00m son % \u001b[32m2\u001b[39m == \u001b[32m0\u001b[39m:\n\u001b[32m      5\u001b[39m             natija += son\n\u001b[32m      6\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m yigindi\n",
      "\u001b[31mTypeError\u001b[39m: 'function' object is not iterable"
     ]
    }
   ],
   "source": [
    "def juft_yigindi(*sonlar):\n",
    "    natija = 0\n",
    "    for son in juft_yigindi:\n",
    "        if son % 2 == 0:\n",
    "            natija += son\n",
    "    return yigindi\n",
    "print(juft_yigindi(1, 2, 3, 4, 5, 6))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "502ff7bf-63a2-44b0-a42b-5c76e544bc53",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "def juft_yigindi(*sonlar):\n",
    "    natija = 0\n",
    "    for son in sonlar:\n",
    "        if son % 2 == 0:\n",
    "            natija += son\n",
    "    return natija\n",
    "print(juft_yigindi(1, 2, 3, 4, 5, 6))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "8499307f-b571-4609-904b-ce0e99003349",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ism: Ali\n",
      "yosh: 25\n",
      "shahar: Toshkent\n"
     ]
    }
   ],
   "source": [
    "def ma_lumot(**kwargs):\n",
    "    for kalit, qiymat in kwargs.items():\n",
    "        print(f\"{kalit}: {qiymat}\")\n",
    "\n",
    "ma_lumot(ism=\"Ali\", yosh=25, shahar=\"Toshkent\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "a44b428d-329d-4ef6-a156-9a2dce245530",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ism: Ali\n",
      "yosh: 25\n",
      "shahar: Toshkent\n"
     ]
    }
   ],
   "source": [
    "def ma_lumot(**betob):\n",
    "    for kalit, qiymat in betob.items():\n",
    "        print(f\"{kalit}: {qiymat}\")\n",
    "\n",
    "ma_lumot(ism=\"Ali\", yosh=25, shahar=\"Toshkent\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "34b1f74e-9661-4359-82bb-02c200f5ec25",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ism:Muslimbek\n",
      "kasb:Developer\n",
      "shahar:Toshkent\n"
     ]
    }
   ],
   "source": [
    "def shaxs_info(**kwargs):\n",
    "    for kalit,qiymat in kwargs.items():\n",
    "        print(f\"{kalit}:{qiymat}\")\n",
    "shaxs_info(ism=\" Muslimbek\", kasb = \" Developer\", shahar = \" Toshkent\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "b3d7756f-62bc-4fde-86c3-7740e02623b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ism: Muslimbek\n",
      "kasb: Developer\n",
      "shahar: Toshkent\n"
     ]
    }
   ],
   "source": [
    "def shaxs_info(**kwargs):\n",
    "    for kalit,qiymat in kwargs.items():\n",
    "        print(f\"{kalit}:{qiymat}\")\n",
    "shaxs_info(ism=\" Muslimbek\", kasb = \" Developer\", shahar = \" Toshkent\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "d15dae9a-adfa-4d6e-84e4-ce9e37d632ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ism: Muslimbek\n",
      "kasb: Developer\n",
      "shahar: Toshkent\n"
     ]
    }
   ],
   "source": [
    "def shaxs_info(**kwargs):\n",
    "    for kalit,qiymat in kwargs.items():\n",
    "        print(f\"{kalit}: {qiymat}\")\n",
    "shaxs_info(ism=\"Muslimbek\", kasb = \"Developer\", shahar = \"Toshkent\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "06e8b2f9-7fca-45e3-af7f-d42efd9b6e0d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ism-->Muslimbek\n",
      "kasb-->Developer\n",
      "shahar-->Toshkent\n"
     ]
    }
   ],
   "source": [
    "def shaxs_info(**kwargs):\n",
    "    for kalit,qiymat in kwargs.items():\n",
    "        print(f\"{kalit} -->{qiymat}\")\n",
    "shaxs_info(ism=\"Muslimbek\", kasb = \"Developer\", shahar = \"Toshkent\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "95a754f8-7f4a-4405-8673-3607cfb0c160",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ism -->Muslimbek\n",
      "kasb -->Developer\n",
      "shahar -->Toshkent\n"
     ]
    }
   ],
   "source": [
    "def shaxs_info(**kwargs):\n",
    "    for kalit,qiymat in kwargs.items():\n",
    "        print(f\"{kalit} -->{qiymat}\")\n",
    "shaxs_info(ism=\"Muslimbek\", kasb = \"Developer\", shahar = \"Toshkent\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "9fcc0102-78c9-4383-a0a9-f5f884369a76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ism --> Muslimbek\n",
      "kasb --> Developer\n",
      "shahar --> Toshkent\n"
     ]
    }
   ],
   "source": [
    "def shaxs_info(**kwargs):\n",
    "    for kalit,qiymat in kwargs.items():\n",
    "        print(f\"{kalit} --> {qiymat}\")\n",
    "shaxs_info(ism=\"Muslimbek\", kasb = \"Developer\", shahar = \"Toshkent\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "2e048a61-2ccf-47fb-a12f-44488a9b64e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(80, 90, 75)\n",
      "{'ism': 'Muslimbek', 'sinf': '11'}\n"
     ]
    }
   ],
   "source": [
    "def add_student(*baholar, **info):\n",
    "    print(baholar)\n",
    "    print(info)\n",
    "add_student(80, 90, 75, ism=\"Muslimbek\", sinf=\"11\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "01097574-2741-4746-8037-de48069e707f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(80, 90, 75)\n",
      "{'ism': 'Muslimbek', 'sinf': '11'}\n"
     ]
    }
   ],
   "source": [
    "def add_student(*baholar, **info):\n",
    "    print(baholar)\n",
    "    print(info)\n",
    "add_student(80, 90, 75, ism=\"Muslimbek\", sinf=\"11\")\n",
    "def add_student(*baholar, **info):\n",
    "    ism = info[\"ism\"]\n",
    "    sinf= info[\"sinf\"]\n",
    "    ortacha = sum(baholar) /len(baholar)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "8ef2d7c5-bdf9-4094-9848-6a1fed0e7d58",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(80, 90, 75)\n",
      "{'ism': 'Muslimbek', 'sinf': '11'}\n",
      "O'tdi\n"
     ]
    }
   ],
   "source": [
    "def add_student(*baholar, **info):\n",
    "    print(baholar)\n",
    "    print(info)\n",
    "add_student(80, 90, 75, ism=\"Muslimbek\", sinf=\"11\")\n",
    "def add_student(*baholar, **info):\n",
    "    ism = info[\"ism\"]\n",
    "    sinf= info[\"sinf\"]\n",
    "    ortacha = sum(baholar) /len(baholar)\n",
    "\n",
    "    if ortacha >= 60:\n",
    "        print(\"O'tdi\")\n",
    "    else:\n",
    "        print(\"Qoldi\")\n",
    "add_student(80, 90, 75, ism=\"Muslimbek\", sinf=\"11\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "809704b0-0e6f-4436-86b5-811c52b504b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "IsmMuslimbek\n",
      "sinf11\n",
      "O'rtacha81.66666666666667\n",
      "holatO'tdi\n"
     ]
    }
   ],
   "source": [
    "def add_student(*baholar, **info):\n",
    "    ism = info[\"ism\"]\n",
    "    sinf = info[\"sinf\"]\n",
    "    ortacha = sum(baholar) / len(baholar)\n",
    "    if ortacha >= 60:\n",
    "        holat = \"O'tdi\"\n",
    "    else:\n",
    "        holat = \"Qoldi\"\n",
    "    \n",
    "    \n",
    "    print(f\"Ism{ism}\")\n",
    "    print(f\"sinf{sinf}\")\n",
    "    print(f\"O'rtacha{ortacha}\")\n",
    "    print(f\"baholar{baholar}\")\n",
    "    print(f\"holat{holat}\")\n",
    "\n",
    "\n",
    "add_student(80, 90, 75, ism=\"Muslimbek\", sinf=\"11\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "41c6b886-2c4d-4c64-9054-e29b0dc92220",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "IsmMuslimbek\n",
      "sinf11\n",
      "O'rtacha81.66666666666667\n",
      "baholar(80, 90, 75)\n",
      "holatO'tdi\n"
     ]
    }
   ],
   "source": [
    "def add_student(*baholar, **info):\n",
    "    ism = info[\"ism\"]\n",
    "    sinf = info[\"sinf\"]\n",
    "    ortacha = sum(baholar) / len(baholar)\n",
    "    if ortacha >= 60:\n",
    "        holat = \"O'tdi\"\n",
    "    else:\n",
    "        holat = \"Qoldi\"\n",
    "    \n",
    "    # shu yerdan o'zing yoz:print\n",
    "    print(f\"Ism{ism}\")\n",
    "    print(f\"sinf{sinf}\")\n",
    "    print(f\"O'rtacha{ortacha}\")\n",
    "    print(f\"baholar{baholar}\")\n",
    "    print(f\"holat{holat}\")\n",
    "\n",
    "\n",
    "add_student(80, 90, 75, ism=\"Muslimbek\", sinf=\"11\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "7df1843f-9081-4d12-8f86-a879a86f6c0d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Baholarni kiriting:  80\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'baholar' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[28]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m kiritma= int(input(\u001b[33m\"Baholarni kiriting: \"\u001b[39m))\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m kiritma = int (baholar)\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m add_student(*baholar, **info):\n\u001b[32m      4\u001b[39m     ism = info[\u001b[33m\"ism\"\u001b[39m]\n\u001b[32m      5\u001b[39m     sinf = info[\u001b[33m\"sinf\"\u001b[39m]\n",
      "\u001b[31mNameError\u001b[39m: name 'baholar' is not defined"
     ]
    }
   ],
   "source": [
    "kiritma= int(input(\"Baholarni kiriting: \"))\n",
    "kiritma = int (baholar)\n",
    "def add_student(*baholar, **info):\n",
    "    ism = info[\"ism\"]\n",
    "    sinf = info[\"sinf\"]\n",
    "    ortacha = sum(baholar) / len(baholar)\n",
    "    if ortacha >= 60:\n",
    "        holat = \"O'tdi\"\n",
    "    else:\n",
    "        holat = \"Qoldi\"\n",
    "\n",
    "    print(f\"Ism: {ism}\")\n",
    "    print(f\"sinf: {sinf}\")\n",
    "    print(f\"O'rtacha: {ortacha}\")\n",
    "    print(f\"baholar: {baholar}\")\n",
    "    print(f\"holat: {holat}\")\n",
    "add_student({kiritma}, ism = \"Muslimbek\", sinf=\"11\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "1ae0c086-60ed-4a8d-af93-e43b0cd237d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Baholarni kiriting:  80,90,65\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: '80,90,65'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mValueError\u001b[39m                                Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[29]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m kiritma= int(input(\u001b[33m\"Baholarni kiriting: \"\u001b[39m))\n\u001b[32m      2\u001b[39m kiritma = int (baholar)\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m add_student(*baholar, **info):\n\u001b[32m      4\u001b[39m     ism = info[\u001b[33m\"ism\"\u001b[39m]\n",
      "\u001b[31mValueError\u001b[39m: invalid literal for int() with base 10: '80,90,65'"
     ]
    }
   ],
   "source": [
    "kiritma= int(input(\"Baholarni kiriting: \"))\n",
    "kiritma = int (baholar)\n",
    "def add_student(*baholar, **info):\n",
    "    ism = info[\"ism\"]\n",
    "    sinf = info[\"sinf\"]\n",
    "    ortacha = sum(baholar) / len(baholar)\n",
    "    if ortacha >= 60:\n",
    "        holat = \"O'tdi\"\n",
    "    else:\n",
    "        holat = \"Qoldi\"\n",
    "\n",
    "    print(f\"Ism: {ism}\")\n",
    "    print(f\"sinf: {sinf}\")\n",
    "    print(f\"O'rtacha: {ortacha}\")\n",
    "    print(f\"baholar: {baholar}\")\n",
    "    print(f\"holat: {holat}\")\n",
    "add_student({kiritma}, ism = \"Muslimbek\", sinf=\"11\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "cf6f5fd2-c70f-486d-ad53-d3def8bb2870",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Baholarni kiriting:  80\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'baholar' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[30]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m kiritma= int(input(\u001b[33m\"Baholarni kiriting: \"\u001b[39m))\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m kiritma = int (baholar)\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m add_student(baholar, **info):\n\u001b[32m      4\u001b[39m     ism = info[\u001b[33m\"ism\"\u001b[39m]\n\u001b[32m      5\u001b[39m     sinf = info[\u001b[33m\"sinf\"\u001b[39m]\n",
      "\u001b[31mNameError\u001b[39m: name 'baholar' is not defined"
     ]
    }
   ],
   "source": [
    "kiritma= int(input(\"Baholarni kiriting: \"))\n",
    "kiritma = int (baholar)\n",
    "def add_student(baholar, **info):\n",
    "    ism = info[\"ism\"]\n",
    "    sinf = info[\"sinf\"]\n",
    "    ortacha = sum(baholar) / len(baholar)\n",
    "    if ortacha >= 60:\n",
    "        holat = \"O'tdi\"\n",
    "    else:\n",
    "        holat = \"Qoldi\"\n",
    "\n",
    "    print(f\"Ism: {ism}\")\n",
    "    print(f\"sinf: {sinf}\")\n",
    "    print(f\"O'rtacha: {ortacha}\")\n",
    "    print(f\"baholar: {baholar}\")\n",
    "    print(f\"holat: {holat}\")\n",
    "add_student({kiritma}, ism = \"Muslimbek\", sinf=\"11\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "cba8de4e-2463-4be0-82ec-cb7a8f0352a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Baholarni kiriting:  80,90,65\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: '80,90,65'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mValueError\u001b[39m                                Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[31]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m kiritma= int(input(\u001b[33m\"Baholarni kiriting: \"\u001b[39m))\n\u001b[32m      2\u001b[39m kiritma = int (baholar)\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m add_student(*baholar, **info):\n\u001b[32m      4\u001b[39m     ism = info[\u001b[33m\"ism\"\u001b[39m]\n",
      "\u001b[31mValueError\u001b[39m: invalid literal for int() with base 10: '80,90,65'"
     ]
    }
   ],
   "source": [
    "kiritma= int(input(\"Baholarni kiriting: \"))\n",
    "kiritma = int (baholar)\n",
    "def add_student(*baholar, **info):\n",
    "    ism = info[\"ism\"]\n",
    "    sinf = info[\"sinf\"]\n",
    "    ortacha = sum(baholar) / len(baholar)\n",
    "    if ortacha >= 60:\n",
    "        holat = \"O'tdi\"\n",
    "    else:\n",
    "        holat = \"Qoldi\"\n",
    "\n",
    "    print(f\"Ism: {ism}\")\n",
    "    print(f\"sinf: {sinf}\")\n",
    "    print(f\"O'rtacha: {ortacha}\")\n",
    "    print(f\"baholar: {baholar}\")\n",
    "    print(f\"holat: {holat}\")\n",
    "add_student(kiritma, ism = \"Muslimbek\", sinf=\"11\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "ac37e597-d4e3-463a-9e21-5d809b3b4ecc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Baholarni kiriting:  80\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'baholar' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[32]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m kiritma= int(input(\u001b[33m\"Baholarni kiriting: \"\u001b[39m))\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m kiritma = int (baholar)\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m add_student(*baholar, **info):\n\u001b[32m      4\u001b[39m     ism = info[\u001b[33m\"ism\"\u001b[39m]\n\u001b[32m      5\u001b[39m     sinf = info[\u001b[33m\"sinf\"\u001b[39m]\n",
      "\u001b[31mNameError\u001b[39m: name 'baholar' is not defined"
     ]
    }
   ],
   "source": [
    "kiritma= int(input(\"Baholarni kiriting: \"))\n",
    "\n",
    "def add_student(*baholar, **info):\n",
    "    ism = info[\"ism\"]\n",
    "    sinf = info[\"sinf\"]\n",
    "    ortacha = sum(baholar) / len(baholar)\n",
    "    if ortacha >= 60:\n",
    "        holat = \"O'tdi\"\n",
    "    else:\n",
    "        holat = \"Qoldi\"\n",
    "\n",
    "    print(f\"Ism: {ism}\")\n",
    "    print(f\"sinf: {sinf}\")\n",
    "    print(f\"O'rtacha: {ortacha}\")\n",
    "    print(f\"baholar: {baholar}\")\n",
    "    print(f\"holat: {holat}\")\n",
    "add_student(kiritma, ism = \"Muslimbek\", sinf=\"11\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "9f1a51dc-3689-4baf-bd87-7eb900752286",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Baholarni kiriting:  80\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ism: Muslimbek\n",
      "sinf: 11\n",
      "O'rtacha: 80.0\n",
      "baholar: (80,)\n",
      "holat: O'tdi\n"
     ]
    }
   ],
   "source": [
    "kiritma= int(input(\"Baholarni kiriting: \"))\n",
    "\n",
    "def add_student(*baholar, **info):\n",
    "    ism = info[\"ism\"]\n",
    "    sinf = info[\"sinf\"]\n",
    "    ortacha = sum(baholar) / len(baholar)\n",
    "    if ortacha >= 60:\n",
    "        holat = \"O'tdi\"\n",
    "    else:\n",
    "        holat = \"Qoldi\"\n",
    "\n",
    "    print(f\"Ism: {ism}\")\n",
    "    print(f\"sinf: {sinf}\")\n",
    "    print(f\"O'rtacha: {ortacha}\")\n",
    "    print(f\"baholar: {baholar}\")\n",
    "    print(f\"holat: {holat}\")\n",
    "add_student(kiritma, ism = \"Muslimbek\", sinf=\"11\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "69b70622-1524-4d4f-96b9-00cf37354b44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Baholarni kiriting:  80, 90, 65\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: '80, 90, 65'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mValueError\u001b[39m                                Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[34]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m kiritma= int(input(\u001b[33m\"Baholarni kiriting: \"\u001b[39m))\n\u001b[32m      2\u001b[39m \n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m add_student(*baholar, **info):\n\u001b[32m      4\u001b[39m     ism = info[\u001b[33m\"ism\"\u001b[39m]\n",
      "\u001b[31mValueError\u001b[39m: invalid literal for int() with base 10: '80, 90, 65'"
     ]
    }
   ],
   "source": [
    "kiritma= int(input(\"Baholarni kiriting: \"))\n",
    "\n",
    "def add_student(*baholar, **info):\n",
    "    ism = info[\"ism\"]\n",
    "    sinf = info[\"sinf\"]\n",
    "    ortacha = sum(baholar) / len(baholar)\n",
    "    if ortacha >= 60:\n",
    "        holat = \"O'tdi\"\n",
    "    else:\n",
    "        holat = \"Qoldi\"\n",
    "\n",
    "    print(f\"Ism: {ism}\")\n",
    "    print(f\"sinf: {sinf}\")\n",
    "    print(f\"O'rtacha: {ortacha}\")\n",
    "    print(f\"baholar: {baholar}\")\n",
    "    print(f\"holat: {holat}\")\n",
    "add_student(*kiritma, ism = \"Muslimbek\", sinf=\"11\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "a8cd5b85-70b0-423f-8822-57e0b1ad347f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1-baho:  80\n",
      "2-baho:  95\n",
      "3-baho:  65\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ism: Muslimbek\n",
      "Sinf: 11\n",
      "O'rtacha: 80.0\n",
      "Baholar: (80, 95, 65)\n",
      "Holat: O'tdi\n"
     ]
    }
   ],
   "source": [
    "b1 = int(input(\"1-baho: \"))\n",
    "b2 = int(input(\"2-baho: \"))\n",
    "b3 = int(input(\"3-baho: \"))\n",
    "\n",
    "def add_student(*baholar, **info):\n",
    "    ism = info[\"ism\"]\n",
    "    sinf = info[\"sinf\"]\n",
    "    ortacha = sum(baholar) / len(baholar)\n",
    "\n",
    "    if ortacha >= 60:\n",
    "        holat = \"O'tdi\"\n",
    "    else:\n",
    "        holat = \"Qoldi\"\n",
    "\n",
    "    print(f\"Ism: {ism}\")\n",
    "    print(f\"Sinf: {sinf}\")\n",
    "    print(f\"O'rtacha: {ortacha}\")\n",
    "    print(f\"Baholar: {baholar}\")\n",
    "    print(f\"Holat: {holat}\")\n",
    "\n",
    "add_student(b1, b2, b3, ism=\"Muslimbek\", sinf=\"11\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a8a43d1-8f40-4296-a090-5f1049592071",
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
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
