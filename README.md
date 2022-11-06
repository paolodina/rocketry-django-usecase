# README.md

## What I need

Regular command fake run.

```bash
$ python manage.py importer
fake run
```

Scheduled command fake run.

```bash
$ python manage.py importer --scheduled
fake run
fake run
fake run
...etc...
```

Regular command real run.

```bash
$ python manage.py importer --real-run
real run
```

Scheduled command real run.

```bash
$ python manage.py importer --real-run --scheduled
real run
real run
real run
...etc...
```

## How I did

https://github.com/paolodina/rocketry-django-usecase/tree/main/usecase/management/commands

Currently I'm "pinning" `args` and `options` using global variables, which looks
ugly (because we are not used to see something like that often?), but it works.

I just wondered it there was a better way (possibily provided by Rocketry) to do
this!

## GitHub refs

- <https://github.com/Miksus/rocketry/issues/76#issuecomment-1302676816>
- <https://github.com/Miksus/rocketry/pull/129/files/00602e1dd69ecbc903d5e1f7e307f10bdb8533e1..e2b2dc0dea6e84a60acb8b4a0e8aa9ecd852beef>
