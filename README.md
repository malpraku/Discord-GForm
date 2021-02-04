# Discord Google Form

Fill your Google Form attendance or any kind as fast as possible, using HTTP Request and Discord Bot, without even needed to open a browser.

## Screenshots
Here are some screenshots on how the bots looks like in both Discord and Google Form Reponses Data. Here are the screenshot of the Discord Application simulating me and how the bot works.

![Discord](https://i.ibb.co/64jKzJN/demo1.jpg)

From above screenshot, you can clearly see I'm sending a form data into the Google Form URL. Now, let's see from the Google Forms owner's side. The response was still recorded though...

![Form](https://i.ibb.co/GsvQZqF/bro2.jpg)

There's no difference between manual input and the Bot input. So, I guess it's worth trying. You can improve the code though. ;)

## Installation

Install Python 3, and use the package manager [pip](https://pip.pypa.io/en/stable/) to install discord.py

```bash
pip install discord.py
```

## Usage
Simply track the post request of the Google Form via the Developer Tools, and change the Bot Token in the code depending on yours!.
```python
# Run the bot with the bot token.
client.run("Change this into your bot token.")
```
