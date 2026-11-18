In my first version, my program could take seven basic registration inputs and print a raw, unformatted summary.

I improved my program by adding string formatting in Version 2 to clean up names and titles, and date formatting in Version 3 to make the event date easy to read.

The string method/function I used was .strip(), .title(), and .upper() because students might type in all lowercase or add accidental spaces, and these methods ensured every registration record looked clean and consistent.

The date/time feature I used was datetime.date and .strftime('%B') because they converted the numeric year, month, and day inputs into a proper, human-readable calendar date like "June 3, 2026".

The biggest change in my program was combining both string manipulation and date/time formatting across multiple versions to turn messy student inputs into a complete, polished registration summary.
