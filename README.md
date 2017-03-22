# Automatic Surf Report Testing

This script requires only requires 3 steps to use and allow you to receive your surf reports.
Full credit for the surf predictions goes to magicseaweed.com.  Thanks to the team over there for giving me an API key to work on this project.
# Setup
### Step 1: Magic Seaweed API
To use this script, you must have a Magic Seaweed API key.
[You can request one here](http://magicseaweed.com/developer/api)

Once you have one, create a config.json file and store the following:
```json
{
  "msw":"{YOUR API KEY}",
  "sender":"{You gmail account}",
  "password":"{Your password}"
}
```
### Step 2: Populate "spots.txt" and "users.txt"
Next, we need to fill up the users.txt file.  This is pretty easy to do.  First we need to find out your providers email to text portal.  For me it's Verizon which uses <yournumber>@vtext.com.
Simply add this postpended to your phone number to users.txt.

Now lets fill spots.txt.  Follow this format:</br>
{Magic Seaweed beach id} {Beach name you want in text}</br>

Example for Del Mar (my favorite beach):</br>
3707 Del Mar

WARNING: malformatting these files will cause the script to crash.  If you can't figure out why it's crashing it could be a newline at the end of the file.  Try to avoid these.

### Step 3: Gmail account
You need a gmail account.  Since most people have one at this point in time, I am not going to go over how to create one.  Simply insert your account into the variable at the top of the python script named

# ENJOY

I hope you enjoy using this script and it always keeps you up to date on the surf report for any given day.  If you come across any issues, please let me know.  Feel free to email me at lukewoodcs@gmail.com

# MIT License

This software is available for use under the MIT License.

 
