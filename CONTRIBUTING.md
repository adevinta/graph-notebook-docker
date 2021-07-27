# Contributing

**This project is in an early stage, we are not accepting external
contributions yet.**

## Workflow

The recommended workflow is feature branching. That means that new features are
developed in branches that are merged to master once they are tested, reviewed
and considered stable.

Small, short-lived and self-contained feature branches along with small pull
requests are recommended. Feature flags are helpful to avoid having very long
lived branches that can be sometimes hard to merge, depending on how quickly
the master branch is updated.

The master branch of this repository is protected. No one is allowed to push
directly to master.

## Commit messages

Commit messages in this project follow a specific set of conventions, which we
discuss in this section.

```
Header line: explain the commit in one line (use the imperative)

Body of commit message is a few lines of text, explaining things
in more detail, possibly giving some background about the issue
being fixed, etc.

The body of the commit message can be several paragraphs, and
please do proper word-wrap and keep columns shorter than about
74 characters or so. That way "git log" will show things
nicely even when it's indented.

Make sure you explain your solution and why you're doing what you're
doing, as opposed to describing what you're doing. Reviewers and your
future self can read the patch, but might not understand why a
particular solution was implemented.
```

The header line of the commit must be prefixed by the primary affected
component followed by colon. If the change affects many components, the
following prefixes are recommended:

- `all`: the change affects many components (e.g. renaming an API)
- `ci`: the change is related to the CI system (e.g. changing `/.travis.yml`)
- `doc`: the change is related to the global documentation (e.g. changing
  `/README.md`)

The body of the commit can be omitted if the header line describes the change
well enough and the pull request message contains the missing details.

## Pull requests

Similarly to what happens with commit messages, pull requests follow a specific
set of conventions.

The title must explain the pull request in one line (use the imperative).

The body of the pull request is a few lines of text, explaining things in more
detail, possibly giving some background about the issue being fixed, etc.

Make sure you explain your solution and why you're doing what you're doing, as
opposed to describing what you're doing. Reviewers and your future self can
read the patch, but might not understand why a particular solution was
implemented.

When a pull request contains several commits, the project does not have to
build and run properly after merging each commit. However, the project must
build and run properly after merging the pull request.

Pull requests must be in a "mergeable" state, pass all the automatic checks and
receive at least +1 from the reviewers before being merged.

When merging pull requests, using merge commits is recommended. That means
that the commits in the pull request must be meaningful and clean.
