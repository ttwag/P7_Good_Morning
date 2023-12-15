# P7_Good_Morning
Automate Python to send a good morning email every day, and the email contains a quote fetched from API.

## How to Use This Program?
### Execution
To use this program to send the quote to a desired email address, you would need
to modify the following items in morning.py to: 
* ```"EMAIL_ADDRESS"```  -> the email address of the sender 
* ```"EMAIL_PASSWORD"``` -> the app password to log in to the sender's email account
* ```"RECEIVER"``` -> the receiver's email address
* ```"QUOTE_API"``` -> the API of the quote provider. I used https://api-ninjas.com/api/quotes.

### Schedule
I used the cron scheduler on macOS to schedule the task to run every morning.

To do so, open terminal and enter ```crontab -e```, then you would see the vim file editor.

This file contains all of your scheduled jobs.

To add one, click ```i``` on the keyboard to start editing and 
follow the template below: 
```
* * * * * command
* - minute (0-59)
* - hour (0-23)
* - day of the month (1-31)
* - month (1-12)
* - day of the week (0-6, 0 is Sunday)
command - command to execute
(from left-to-right)
```

For example, if I want to schedule morning.py to run every morning at 6:00 am on every day of the year, I would write

```0 6 * * * /opt/homebrew/bin/python3.11 $HOME/Desktop/Project/P7_Good_Morning/morning.py```

After the editing is done, hit ```etc``` then enter ```:wq``` to save and exit the vim editor.  

## File Structure
morning.py fetches the quote from API then email the desired account. It depends on the **dotenv** library.

## Note
If you use a gmail account to send the email, enable that gmail address to use app password to log in and input 
that app password to the program as stated in How to Use This Program section.