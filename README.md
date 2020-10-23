# PW4py: Politics & War API wrapper for Python

---

### - This project is abandoned, though you are welcome to fork it and continue. -

---

### Currently Implemented API Endpoints
* **Unauthenticated APIs:**
    - Nation API
    - Alliance API
    - *work still in progress*

* **Authenticated APIs:**
    - *none, work still in progress*

### Features
- Easy to use
- Object oriented *(take this with a grain of salt, it's my first OOP project xD)*
- No need worry about Alex's inability to use correct typing 🙄
- ~~Built-in cache for better performance in non-time-critical APIs~~ *in progress*
- ~~Supports both `requests` and `aiohttp` backends~~ *in progress*

### Installation
PW4py is now on [PyPI](https://pypi.org/project/PW4py/), so you can just install it by doing:
```bash
pip install pw4py
```

### Usage
1. Load it:
    ```py
    import pw4py

    # default
    pw4py.init(key = "abcdef12345")
    # use the test server
    pw4py.load(test_server = True, key = "abcdef12345")
    ```
2. Init an object of the API you want to use:
    ```py
    from pw4py import Nation    # so you don't have to type pw4py.Nation() every time

    nation = Nation(id)
    ```
3. Use it!
    ```py
    name = str(nation)
    cityids = nation.cityids
    color = nation.get("color")
    # etc...
    ```

### Issues or suggestions
Feel free to make a new issue [here](https://gitlab.com/jdtech/pw4py/issues) if you find any bugs, encounter any problems, or have a feature suggestion.
If you know how to fix it or how to implement a new feature, please do! Fork the repo, and submit a pull request :)
