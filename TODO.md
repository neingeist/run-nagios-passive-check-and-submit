- Support submitting host checks
- Do not color output when stdout is not a tty
- Add a --retry=n option to retry check n times
- Handle errors issued by the CGI, e.g.:

    `<DIV CLASS='errorMessage'>
    Sorry, but you are not authorized to commit the specified command.
    </DIV>`
