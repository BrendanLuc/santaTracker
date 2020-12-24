on run {targetPhone, Message}
  tell application "Messages"
    set targetService to 1st service whose service type = iMessage
    set targetBuddy to buddy targetPhone of targetService
    set targetMessage to Message
    send targetMessage to targetBuddy
  end tell
end run
