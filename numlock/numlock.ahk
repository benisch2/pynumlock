; Numlock.ahk -> Very Simple. Pushes the Numlock Key!

#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

Send {NumLock} ; Press numberlock

return ; End script

ExitApp ; Exit AHK Application