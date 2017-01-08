# -*- coding: utf-8 -*-
import os

from invoke import task, run

docs_dir = 'docs'
build_dir = os.path.join(docs_dir, '_build')


@task
def test(context):
    run('python setup.py test', pty=True)


@task
def clean(context):
    run("rm -rf build")
    run("rm -rf dist")
    run("rm -rf instaread.egg-info")
    clean_docs(context)
    print("Cleaned up.")


@task
def clean_docs(context):
    run("rm -rf %s" % build_dir)


@task
def browse_docs(context):
    run("open %s" % os.path.join(build_dir, 'index.html'))


@task
def build_docs(context, clean=False, browse=False):
    if clean:
        clean_docs(context)
    run("sphinx-build %s %s" % (docs_dir, build_dir), pty=True)
    if browse:
        browse_docs(context)


@task
def readme(context, browse=False):
    run('rst2html.py README.rst > README.html')


@task
def publish(context, test=False):
    """Publish to the cheeseshop."""
    if test:
        run('python setup.py register -r test sdist upload -r test')
    else:
        run("python setup.py register sdist upload")
