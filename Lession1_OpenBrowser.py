import webbrowser
import time

url = 'http://www.python.org/'


count = 0
while (count < 3):
    time.sleep(10)
    # Open URL in a new tab, if a browser window is already open.
    webbrowser.open_new_tab(url + 'doc/')
    # Open URL in new window, raising the window if possible.
    webbrowser.open_new(url)
    count += 1

print 'Good Bye'
