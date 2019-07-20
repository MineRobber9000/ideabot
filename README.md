# ideabot

A standalone bot form of a word ideas plugin I wrote for my IRC bot, 
[minerbot2](https://tildegit.org/khuxkm/minerbot2).

## How it works

It uses the `teambot` library I created to take messages from IRC. It then uses 
ArgumentParser to parse the set and count arguments (defaulting to 3 words of 
the `common` set) and display said words in a fancy way.

```
> !idea
< How about a story with the words "there", "wednesday", and "film"?
> !idea -s dinosaurs 10
< How about a story with the words "Leyesaurus", "Auroraceratops", 
"Geminiraptor", "Vulcanodon", "Melanorosaurus", "Auroraceratops", "Leyesaurus", 
"Yunnanosaurus", "Erliansaurus", and "Mtapaiasaurus"?
```
