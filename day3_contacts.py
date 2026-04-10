{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4bd71cc0-6b77-4521-bfbf-512c916515c1",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3395382840.py, line 4)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 4\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mexcept ValueError:\u001b[39m\n    ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    ism =  input(\"Ismingizni kiriting: \")\n",
    "    yosh = int(input(\"Yoshingizni kiriting: \"))\n",
    "except ValueError:\n",
    "    print(\"Son kiriting!\")\n",
    "    \n",
    "\n",
    "\n",
    "if yosh =< 0:\n",
    "    print(\"Yosh manfiy bo'lmaydi!\")\n",
    "else:\n",
    "    print(\"Salom, [ism]! Yoshingiz: [yosh]\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "920e4bc7-1e12-411b-a00b-20442f210850",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3610477490.py, line 9)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 9\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mif yosh =< 0:\u001b[39m\n            ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    ism =  input(\"Ismingizni kiriting: \")\n",
    "    yosh = int(input(\"Yoshingizni kiriting: \"))\n",
    "except ValueError:\n",
    "    print(\"Son kiriting!\")\n",
    "    \n",
    "\n",
    "\n",
    "if yosh =< 0:\n",
    "    print(\"Yosh manfiy bo'lmaydi!\")\n",
    "else:\n",
    "    print(\"Salom, [ism]! Yoshingiz: [yosh]\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b6940d88-b2e0-4be9-9e18-30b00cdcb53d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ismingizni kiriting:  Otabek\n",
      "Yoshingizni kiriting:  Otabek\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Son kiriting!\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'yosh' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[3]\u001b[39m\u001b[32m, line 9\u001b[39m\n\u001b[32m      5\u001b[39m     print(\u001b[33m\"Son kiriting!\"\u001b[39m)\n\u001b[32m      6\u001b[39m \n\u001b[32m      7\u001b[39m \n\u001b[32m      8\u001b[39m \n\u001b[32m----> \u001b[39m\u001b[32m9\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m yosh <= \u001b[32m0\u001b[39m:\n\u001b[32m     10\u001b[39m     print(\u001b[33m\"Yosh manfiy bo'lmaydi!\"\u001b[39m)\n\u001b[32m     11\u001b[39m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m     12\u001b[39m     print(\u001b[33m\"Salom, [ism]! Yoshingiz: [yosh]\"\u001b[39m)\n",
      "\u001b[31mNameError\u001b[39m: name 'yosh' is not defined"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    ism =  input(\"Ismingizni kiriting: \")\n",
    "    yosh = int(input(\"Yoshingizni kiriting: \"))\n",
    "except ValueError:\n",
    "    print(\"Son kiriting!\")\n",
    "    \n",
    "\n",
    "\n",
    "if yosh <= 0:\n",
    "    print(\"Yosh manfiy bo'lmaydi!\")\n",
    "else:\n",
    "    print(\"Salom, [ism]! Yoshingiz: [yosh]\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "47aed784-1edf-4c47-a45f-c891edc88422",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ismingizni kiriting:  Otabek\n",
      "Yoshingizni kiriting:  22\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Salom, [ism]! Yoshingiz: [yosh]\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    ism =  input(\"Ismingizni kiriting: \")\n",
    "    yosh = int(input(\"Yoshingizni kiriting: \"))\n",
    "except ValueError:\n",
    "    print(\"Son kiriting!\")\n",
    "    \n",
    "\n",
    "\n",
    "if yosh <= 0:\n",
    "    print(\"Yosh manfiy bo'lmaydi!\")\n",
    "else:\n",
    "    print(\"Salom, [ism]! Yoshingiz: [yosh]\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8a979693-3665-4e62-84a9-c6ca141795c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ismingizni kiriting:  otabek\n",
      "Yoshingizni kiriting:  22\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Salom ['otabek'] Yoshingiz:  [22]\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    ism =  input(\"Ismingizni kiriting: \")\n",
    "    yosh = int(input(\"Yoshingizni kiriting: \"))\n",
    "except ValueError:\n",
    "    print(\"Son kiriting!\")\n",
    "    \n",
    "\n",
    "\n",
    "if yosh <= 0:\n",
    "    print(\"Yosh manfiy bo'lmaydi!\")\n",
    "else:\n",
    "    print(\"Salom\", [ism], \"Yoshingiz: \", [yosh])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8c7b99fe-956a-4c13-9a86-572a43243ecc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ismingizni kiriting:  Otabek\n",
      "Yoshingizni kiriting:  22\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Salom Otabek Yoshingiz:  22\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    ism =  input(\"Ismingizni kiriting: \")\n",
    "    yosh = int(input(\"Yoshingizni kiriting: \"))\n",
    "except ValueError:\n",
    "    print(\"Son kiriting!\")\n",
    "    \n",
    "\n",
    "\n",
    "if yosh <= 0:\n",
    "    print(\"Yosh manfiy bo'lmaydi!\")\n",
    "else:\n",
    "    print(\"Salom\", ism, \"Yoshingiz: \", yosh)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a78d6adf-7f98-4631-87c5-c3520d44a162",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ismingizni kiriting:  Otabek\n",
      "Yoshingizni kiriting:  abc\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Son kiriting!\n",
      "Salom Otabek Yoshingiz:  22\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    ism =  input(\"Ismingizni kiriting: \")\n",
    "    yosh = int(input(\"Yoshingizni kiriting: \"))\n",
    "except ValueError:\n",
    "    print(\"Son kiriting!\")\n",
    "    \n",
    "\n",
    "\n",
    "if yosh <= 0:\n",
    "    print(\"Yosh manfiy bo'lmaydi!\")\n",
    "else:\n",
    "    print(\"Salom\", ism, \"Yoshingiz: \", yosh)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0934335a-bb9e-446f-8401-f66290216416",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ismingizni kiriting:  otabek\n",
      "Yoshingizni kiriting:  abc\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Son kiriting!\n",
      "Salom otabek! Yoshingiz: 22\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    ism = input(\"Ismingizni kiriting: \")\n",
    "    yosh = int(input(\"Yoshingizni kiriting: \n",
    "    if yosh <= 0:\n",
    "        print(\"Yosh manfiy bo'lmaydi!\")\n",
    "    else:\n",
    "    print(f\"Salom {ism}! Yoshingiz: {yosh}\")\n",
    "except ValueError:\n",
    "    print(\"Son kiriting!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "14b04e22-c9a6-4320-a5b2-d80285203d73",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unterminated string literal (detected at line 3) (2388376616.py, line 3)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[9]\u001b[39m\u001b[32m, line 3\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31myosh = int(input(\"Yoshingizni kiriting:\u001b[39m\n                     ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m unterminated string literal (detected at line 3)\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    ism = input(\"Ismingizni kiriting: \")\n",
    "    yosh = int(input(\"Yoshingizni kiriting: \n",
    "    if yosh <= 0:\n",
    "        print(\"Yosh manfiy bo'lmaydi!\")\n",
    "    else:\n",
    "    print(f\"Salom {ism}! Yoshingiz: {yosh}\")\n",
    "except ValueError:\n",
    "    print(\"Son kiriting!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "fded7f6e-7015-4ec4-a313-3ba2e5ae097d",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block after 'else' statement on line 6 (4023361477.py, line 7)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[10]\u001b[39m\u001b[32m, line 7\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mprint(f\"Salom {ism}! Yoshingiz: {yosh}\")\u001b[39m\n    ^\n\u001b[31mIndentationError\u001b[39m\u001b[31m:\u001b[39m expected an indented block after 'else' statement on line 6\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    ism = input(\"Ismingizni kiriting: \")\n",
    "    yosh = int(input(\"Yoshingizni kiriting: \"))\n",
    "    if yosh <= 0:\n",
    "        print(\"Yosh manfiy bo'lmaydi!\")\n",
    "    else:\n",
    "    print(f\"Salom {ism}! Yoshingiz: {yosh}\")\n",
    "except ValueError:\n",
    "    print(\"Son kiriting!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "84b4dfbb-0fc8-47a2-b5ad-d3bb6e7dd335",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ismingizni kiriting:  otabek\n",
      "Yoshingizni kiriting:  22\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Salom otabek! Yoshingiz: 22\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    ism = input(\"Ismingizni kiriting: \")\n",
    "    yosh = int(input(\"Yoshingizni kiriting: \"))\n",
    "    if yosh <= 0:\n",
    "        print(\"Yosh manfiy bo'lmaydi!\")\n",
    "    else:\n",
    "        print(f\"Salom {ism}! Yoshingiz: {yosh}\")\n",
    "except ValueError:\n",
    "    print(\"Son kiriting!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "5e9281d3-2d21-4fb7-b9c2-545bcf5c62b8",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax. Maybe you meant '==' or ':=' instead of '='? (3858917525.py, line 6)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[12]\u001b[39m\u001b[32m, line 6\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mism = input(\"Ismingizni kiriting: \")\u001b[39m\n    ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m invalid syntax. Maybe you meant '==' or ':=' instead of '='?\n"
     ]
    }
   ],
   "source": [
    "###mmini project in the end of day\n",
    "\n",
    "import json as js \n",
    "\n",
    "malumot = {\n",
    "    ism = input(\"Ismingizni kiriting: \")\n",
    "    yosh = int(input(\"Yoshingizni kiritng: \"))\n",
    "    tefon = int(input(\"Telef raqamingizni kiritng: \"))\n",
    "}\n",
    "with open(\"malumot.json\", \"w\") as f:\n",
    "    js.dumb(malumot, f)\n",
    "with open(\"malumot.json\", \"r\") as f:\n",
    "    data = js.load(f)\n",
    "\n",
    "print(data)\n",
    "print(data[\"ism\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e63699a9-fcc4-4d13-a58c-bc38ba487eb7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ismingizni kiriting:  otabek\n",
      "Yoshingizni kiriting:  22\n",
      "Telefon raqamingizni kiriting:  908778787\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'ism': 'otabek', 'yosh': 22, 'telefon': 908778787}\n"
     ]
    },
    {
     "ename": "KeyError",
     "evalue": "('ism', 'yosh', 'telefon')",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mKeyError\u001b[39m                                  Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[13]\u001b[39m\u001b[32m, line 15\u001b[39m\n\u001b[32m     11\u001b[39m     js.dump(malumot, f)\n\u001b[32m     12\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m open(\u001b[33m\"malumot.json\"\u001b[39m, \u001b[33m\"r\"\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[32m     13\u001b[39m     data = js.load(f)\n\u001b[32m     14\u001b[39m print(data)\n\u001b[32m---> \u001b[39m\u001b[32m15\u001b[39m print(data[\u001b[33m\"ism\"\u001b[39m, \u001b[33m\"yosh\"\u001b[39m, \u001b[33m\"telefon\"\u001b[39m])\n",
      "\u001b[31mKeyError\u001b[39m: ('ism', 'yosh', 'telefon')"
     ]
    }
   ],
   "source": [
    "import json as js\n",
    "\n",
    "ism = input(\"Ismingizni kiriting: \")\n",
    "yosh = int(input(\"Yoshingizni kiriting: \"))\n",
    "telefon = int(input(\"Telefon raqamingizni kiriting: \"))\n",
    "\n",
    "malumot = {\n",
    "    \"ism\": ism, \"yosh\": yosh, \"telefon\": telefon\n",
    "}\n",
    "with open(\"malumot.json\", \"w\") as f:\n",
    "    js.dump(malumot, f)\n",
    "with open(\"malumot.json\", \"r\") as f:\n",
    "    data = js.load(f)\n",
    "print(data)\n",
    "print(data[\"ism\", ])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f5d631d6-0ce4-4db6-8e45-e920fab5ee57",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ismingizni kiriting:  otabek\n",
      "Yoshingizni kiriting:  yosh\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: 'yosh'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mValueError\u001b[39m                                Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[14]\u001b[39m\u001b[32m, line 4\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m json \u001b[38;5;28;01mas\u001b[39;00m js\n\u001b[32m      2\u001b[39m \n\u001b[32m      3\u001b[39m ism = input(\u001b[33m\"Ismingizni kiriting: \"\u001b[39m)\n\u001b[32m----> \u001b[39m\u001b[32m4\u001b[39m yosh = int(input(\u001b[33m\"Yoshingizni kiriting: \"\u001b[39m))\n\u001b[32m      5\u001b[39m telefon = int(input(\u001b[33m\"Telefon raqamingizni kiriting: \"\u001b[39m))\n\u001b[32m      6\u001b[39m \n\u001b[32m      7\u001b[39m malumot = {\n",
      "\u001b[31mValueError\u001b[39m: invalid literal for int() with base 10: 'yosh'"
     ]
    }
   ],
   "source": [
    "import json as js\n",
    "\n",
    "ism = input(\"Ismingizni kiriting: \")\n",
    "yosh = int(input(\"Yoshingizni kiriting: \"))\n",
    "telefon = int(input(\"Telefon raqamingizni kiriting: \"))\n",
    "\n",
    "malumot = {\n",
    "    \"ism\": ism, \"yosh\": yosh, \"telefon\": telefon\n",
    "}\n",
    "with open(\"malumot.json\", \"w\") as f:\n",
    "    js.dump(malumot, f)\n",
    "with open(\"malumot.json\", \"r\") as f:\n",
    "    data = js.load(f)\n",
    "print(data)\n",
    "print(data[\"ism\", ])\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "40988c75-4773-4191-bdaf-af2f16859bc2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ismingizni kiriting:  otabek\n",
      "Yoshingizni kiriting:  22\n",
      "Telefon raqamingizni kiriting:  9098983829\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'ism': 'otabek', 'yosh': 22, 'telefon': 9098983829}\n"
     ]
    },
    {
     "ename": "KeyError",
     "evalue": "('ism',)",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mKeyError\u001b[39m                                  Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[15]\u001b[39m\u001b[32m, line 15\u001b[39m\n\u001b[32m     11\u001b[39m     js.dump(malumot, f)\n\u001b[32m     12\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m open(\u001b[33m\"malumot.json\"\u001b[39m, \u001b[33m\"r\"\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[32m     13\u001b[39m     data = js.load(f)\n\u001b[32m     14\u001b[39m print(data)\n\u001b[32m---> \u001b[39m\u001b[32m15\u001b[39m print(data[\u001b[33m\"ism\"\u001b[39m, ])\n",
      "\u001b[31mKeyError\u001b[39m: ('ism',)"
     ]
    }
   ],
   "source": [
    "import json as js\n",
    "\n",
    "ism = input(\"Ismingizni kiriting: \")\n",
    "yosh = int(input(\"Yoshingizni kiriting: \"))\n",
    "telefon = int(input(\"Telefon raqamingizni kiriting: \"))\n",
    "\n",
    "malumot = {\n",
    "    \"ism\": ism, \"yosh\": yosh, \"telefon\": telefon\n",
    "}\n",
    "with open(\"malumot.json\", \"w\") as f:\n",
    "    js.dump(malumot, f)\n",
    "with open(\"malumot.json\", \"r\") as f:\n",
    "    data = js.load(f)\n",
    "print(data)\n",
    "print(data[\"ism\", ])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "28097d29-8407-4231-9b8e-7bdf2fad23e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ismingizni kiriting:  otabek\n",
      "Yoshingizni kiriting:  22\n",
      "Telefon raqamingizni kiriting:  909090909\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'ism': 'otabek', 'yosh': 22, 'telefon': 909090909}\n",
      "otabek\n"
     ]
    }
   ],
   "source": [
    "import json as js\n",
    "\n",
    "ism = input(\"Ismingizni kiriting: \")\n",
    "yosh = int(input(\"Yoshingizni kiriting: \"))\n",
    "telefon = int(input(\"Telefon raqamingizni kiriting: \"))\n",
    "\n",
    "malumot = {\n",
    "    \"ism\": ism, \"yosh\": yosh, \"telefon\": telefon\n",
    "}\n",
    "with open(\"malumot.json\", \"w\") as f:\n",
    "    js.dump(malumot, f)\n",
    "with open(\"malumot.json\", \"r\") as f:\n",
    "    data = js.load(f)\n",
    "print(data)\n",
    "print(data[\"ism\"])\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "2fc86303-ba0d-407d-9aa4-83ce154f11a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "1. Kontakt qo'sh\n",
      "2. Kontaktlarni ko'rsat\n",
      "3. Chiq\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Tanlov:  1\n",
      "Ism:  Otabek\n",
      "Telefon:  909099999\n",
      "Yosh:  22\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Saqlandi!\n",
      "\n",
      "1. Kontakt qo'sh\n",
      "2. Kontaktlarni ko'rsat\n",
      "3. Chiq\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Tanlov:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1. Otabek — 909099999 — 22 yosh\n",
      "\n",
      "1. Kontakt qo'sh\n",
      "2. Kontaktlarni ko'rsat\n",
      "3. Chiq\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Tanlov:  3\n"
     ]
    }
   ],
   "source": [
    "import json as js\n",
    "\n",
    "def kontaktlarni_yukla():\n",
    "    try:\n",
    "        with open(\"kontaktlar.json\", \"r\") as f:\n",
    "            return js.load(f)\n",
    "    except FileNotFoundError:\n",
    "        return []\n",
    "\n",
    "def kontaktlarni_saqlа(kontaktlar):\n",
    "    with open(\"kontaktlar.json\", \"w\") as f:\n",
    "        js.dump(kontaktlar, f)\n",
    "\n",
    "kontaktlar = kontaktlarni_yukla()\n",
    "\n",
    "while True:\n",
    "    print(\"\\n1. Kontakt qo'sh\")\n",
    "    print(\"2. Kontaktlarni ko'rsat\")\n",
    "    print(\"3. Chiq\")\n",
    "    \n",
    "    tanlov = input(\"Tanlov: \")\n",
    "    \n",
    "    if tanlov == \"1\":\n",
    "        ism = input(\"Ism: \")\n",
    "        telefon = input(\"Telefon: \")\n",
    "        yosh = int(input(\"Yosh: \"))\n",
    "        kontaktlar.append({\"ism\": ism, \"telefon\": telefon, \"yosh\": yosh})\n",
    "        kontaktlarni_saqlа(kontaktlar)\n",
    "        print(\"Saqlandi!\")\n",
    "    \n",
    "    elif tanlov == \"2\":\n",
    "        for i, k in enumerate(kontaktlar, 1):\n",
    "            print(f\"{i}. {k['ism']} — {k['telefon']} — {k['yosh']} yosh\")\n",
    "    \n",
    "    elif tanlov == \"3\":\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "1445a014-c68f-42f7-aed2-ee7fb2b43e10",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "expected ':' (3010763225.py, line 35)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[18]\u001b[39m\u001b[32m, line 35\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31melse tanlov == \"3\":\u001b[39m\n         ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m expected ':'\n"
     ]
    }
   ],
   "source": [
    "import json as js\n",
    "\n",
    "def kontaktlarni_yukla():\n",
    "    try:\n",
    "        with open(\"kontaktlar.json\", \"r\") as f:\n",
    "            return js.load(f)\n",
    "    except FileNotFoundError:\n",
    "        return []\n",
    "\n",
    "def kontaktlarni_saqlа(kontaktlar):\n",
    "    with open(\"kontaktlar.json\", \"w\") as f:\n",
    "        js.dump(kontaktlar, f)\n",
    "\n",
    "kontaktlar = kontaktlarni_yukla()\n",
    "\n",
    "while True:\n",
    "    print(\"\\n1. Kontakt qo'sh\")\n",
    "    print(\"2. Kontaktlarni ko'rsat\")\n",
    "    print(\"3. Chiq\")\n",
    "    \n",
    "    tanlov = input(\"Tanlov: \")\n",
    "    \n",
    "    if tanlov == \"1\":\n",
    "        ism = input(\"Ism: \")\n",
    "        telefon = input(\"Telefon: \")\n",
    "        yosh = int(input(\"Yosh: \"))\n",
    "        kontaktlar.append({\"ism\": ism, \"telefon\": telefon, \"yosh\": yosh})\n",
    "        kontaktlarni_saqlа(kontaktlar)\n",
    "        print(\"Saqlandi!\")\n",
    "    \n",
    "    elif tanlov == \"2\":\n",
    "        for i, k in enumerate(kontaktlar, 1):\n",
    "            print(f\"{i}. {k['ism']} — {k['telefon']} — {k['yosh']} yosh\")\n",
    "    \n",
    "    else tanlov == \"3\":\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e5059349-6dac-4ba5-be21-c4aa575dd73e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "1. Kontakt qo'sh\n",
      "2. Kontaktlarni ko'rsat\n",
      "3. Chiq\n"
     ]
    }
   ],
   "source": [
    "import json as js\n",
    "\n",
    "def kontaktlarni_yukla():\n",
    "    try:\n",
    "        with open(\"kontaktlar.json\", \"r\") as f:\n",
    "            return js.load(f)\n",
    "    except FileNotFoundError:\n",
    "        return []\n",
    "\n",
    "def kontaktlarni_saqlа(kontaktlar):\n",
    "    with open(\"kontaktlar.json\", \"w\") as f:\n",
    "        js.dump(kontaktlar, f)\n",
    "\n",
    "kontaktlar = kontaktlarni_yukla()\n",
    "\n",
    "while True:\n",
    "    print(\"\\n1. Kontakt qo'sh\")\n",
    "    print(\"2. Kontaktlarni ko'rsat\")\n",
    "    print(\"3. Chiq\")\n",
    "    \n",
    "    tanlov = input(\"Tanlov: \")\n",
    "    \n",
    "    if tanlov == \"1\":\n",
    "        ism = input(\"Ism: \")\n",
    "        telefon = input(\"Telefon: \")\n",
    "        yosh = int(input(\"Yosh: \"))\n",
    "        kontaktlar.append({\"ism\": ism, \"telefon\": telefon, \"yosh\": yosh})\n",
    "        kontaktlarni_saqlа(kontaktlar)\n",
    "        print(\"Saqlandi!\")\n",
    "    \n",
    "    elif tanlov == \"2\":\n",
    "        for i, k in enumerate(kontaktlar, 1):\n",
    "            print(f\"{i}. {k['ism']} — {k['telefon']} — {k['yosh']} yosh\")\n",
    "    \n",
    "    elif tanlov == \"3\":\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7b281ec9-99d9-486f-b6cf-679c5c882db3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json as js\n",
    "def kontakt_yukla():\n",
    "    try:\n",
    "        with open(\"kontaktlar.json\", \"r\") as f:\n",
    "            return js.load(f)\n",
    "    except FileNotFoundError:\n",
    "        return []\n",
    "def kontaktlarni_saqla():\n",
    "    with open(\"kontaktlar.json\" \"w\") as f:\n",
    "        js.dumb(kontaktlar, f)\n",
    "kontaktlar = kontaktlarni_yukla()\n",
    "\n",
    "while True:\n",
    "    print(\"\\n1. Kontakt qo'sh\")\n",
    "    print(\"\\n2. Kontakt ber\")\n",
    "    print(\"\\n3. Chiq\")\n",
    "\n",
    "    tanlov = input(\"Tanlov: \")\n",
    "\n",
    "    if tanlov == \"1\":\n",
    "        ism = input(\"Ism: \")\n",
    "        telefon = int(input(\"Telefon: \"))\n",
    "        yosh = int(input(\"Yosh: \"))\n",
    "        kontaktlar.append({\"ism\": ism, \"telefon\": telefon, \"yosh\": yosh})\n",
    "        kontaktlarni_saqla(kontaktlar)\n",
    "        print(\"Saqlandi\")\n",
    "    elif tanlov == \"2\":\n",
    "        for i, k in enumerate(kontaktlar, 1):\n",
    "            print(f\"{i}. {k['ism']} — {k['telefon']} — {k['yosh']} yosh\")\n",
    "    elif tanlov == \"3\":\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c5cc8994-52d7-455b-91b0-6d02cc7765b9",
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
