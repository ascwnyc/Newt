# Newt

Newt is a multi-purpose Discord bot designed in Python.

## Foreword

The main design principles for Newt trend towards general functionality, simplicity in interfacing with users, and a narrowed focus of its detailed feature set.

It is planned sometime in the future to convert the project's language to JavaScript, and then TypeScript. This change is mainly comes from the longevity the program will have in a web-based language like JavaScript, and it's compatability with a web-based API like Discord.

***Note:** Newt is very much still a work-in-progress. Any and all functionality is subject ot change.*

## Notes

Below is some context to what this program does. This information is relevant to employers and/or those interested in what the code actually does when its all put together.

- **Cogs:** The cogs folder contains a set of .py files which act as individual modules that plug in to the main.py program. Discord's API supports loading and unloading individual module functionality through a term they call 'cogs', hence the name of the folder. Cogs essentially provide a lot of control over what features of a bot you want loaded at a given time.
- Almost all of the customisation side of the program's functionality is controlled through a .py file called 'config.py'. It contains variables that reference colours for styling embedded message functions, .env environment variables that are important to keep hidden from the public, and other variables that generally are used to control the properties of the program from one place, rather than having to delve into the code of other files to edit customisable parts of the program.
