# Pre-Commit Hook: Convert indents (from spaces) to tabs

## Project Rationale

I created this project as a reaction to the Terraform autoformatter.
However, the project can be used in other circumstances.

Autoformatters are great. However, Terraform's `fmt` command indents
code using two-spaces. I have a mild visual impairment, and a two-space
indent is difficult for me.

I want to benefit from all of the other work the autoformatter is doing
for me, and I simply want to replace the space indents with tabs. I
don't want to create my own autoformatter. This pre-commit hook is meant
to be run after the autoformatter to achieve these goals.

Philosophically speaking: Tabs are for indents. Spaces are for
alignment. Tabs allow people to set their own preference, a necessity
for those with different needs.

I hope this helps others with eye issues.
