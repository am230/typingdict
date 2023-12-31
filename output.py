from typing import List, Dict, Union, TypedDict, Optional


class Address(TypedDict):
    street: 'str'
    city: 'str'
    state: 'str'
    zipCode: 'str'


class FriendsItem(TypedDict):
    name: 'str'
    age: 'int'
    isStudent: 'bool'
    favoriteFruits: 'List[str]'
    address: 'Address'


class Root(TypedDict):
    name: 'str'
    age: 'int'
    isStudent: 'bool'
    favoriteFruits: 'List[str]'
    address: 'Address'
    friends: 'List[FriendsItem]'

