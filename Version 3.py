from datetime import date

first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
section = input("Enter section: ").strip()
event_name = input("Enter event name: ").strip()
event_year = int(input("Enter event year: "))
event_month = int(input("Enter event month: "))
event_day = int(input("Enter event day: "))

full_name = first_name + " " + last_name
proper_name = full_name.title()
name_code = full_name.upper()
clean_section = section.upper()
clean_event = event_name.title()

event_date = date(event_year, event_month, event_day)
readable_date = f"{event_date.strftime('%B')} {event_date.day}, {event_date.year}"

print("\nStudent Event Registration Summary")
print("Name:", proper_name)
print("Name Code:", name_code)
print("Section:", clean_section)
print("Event:", clean_event)
print("Event Date:", readable_date)
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")
print("Registration record created successfully.")
