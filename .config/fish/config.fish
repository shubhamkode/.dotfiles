set fish_greeting

fundle plugin oh-my-fish/theme-l
fundle plugin markcial/upto
fundle plugin jethrokuan/z
fundle plugin tuvistavie/fish-fastdir

fundle init

# bun
set --export BUN_INSTALL "$HOME/.bun"
set --export PATH $BUN_INSTALL/bin $PATH
