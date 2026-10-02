# Brewsite

Brewsite is a Python Flask project I am building for **ICT 362 - Software Technology II at NMSU**.

The main goal of the project is to get more practice with Flask, templates, testing, Git, and using different branches like `development`, `staging`, and `production`.

The GitHub Actions and Microsoft Teams notifications were not required for the class. I added those as a side project because I wanted more practice with CI/CD and DevOps workflows.

## Technologies Used

- Python 3.11
- Flask
- Bootstrap 5
- Pytest
- Git
- GitHub
- GitHub Actions
- Microsoft Teams Workflows

## Project Structure

```text
Brewsite/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── brewsite.py
│   └── templates/
│       ├── base.html
│       ├── home.html
│       ├── breweries.html
│       ├── beer_types.html
│       └── about.html
├── test/
│   ├── __init__.py
│   └── test_integrated.py
├── requirements.txt
└── README.md
```

## Branch Workflow

For class we are learning how to work with three main branches:

```text
development
    ↓
staging
    ↓
production
```

### Development

`development` is where I make changes and test new code first.

This is the branch I normally work from before I try to move anything forward.

### Staging

`staging` is the part that confused me a little at first.

The way I understand it now is that staging is basically the last checkpoint before production.

The code should already be working in development before it gets moved to staging. Once it is in staging, it is treated more like a release candidate and gets checked again before production.

For this project, staging is currently a Git branch and a GitHub Environment. I do not have a separate staging server running the Flask app yet.

### Production

`production` is the stable version of the project.

Code should only make it here after it has already passed through development and staging.

## Pull Request Flow

I added Pull Requests and GitHub rulesets so I could practice a more controlled workflow.

The flow is:

```text
development
    ↓
Pull Request
    ↓
Run Flask Tests
    ↓
staging
    ↓
Pull Request
    ↓
Run Flask Tests
    ↓
production
```

Both `staging` and `production` have rules that require the Flask tests to pass before the Pull Request can be merged.

I also blocked force pushes and restricted deleting those branches.

## Testing

The project uses Pytest for integration testing.

One of the tests creates a Flask test client and checks that the home page responds correctly.

```python
from app.brewsite import app


def test_client():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Brewery" in response.data
```

To run the tests locally:

```bash
pytest -v
```


## What GitHub Actions Is

GitHub Actions is the part of GitHub that runs automated jobs when something happens in the repository.

The easiest way for me to understand it is to compare it to Jenkins because I have some experience seeing Jenkins pipelines at work.

With Jenkins, a pipeline might pull the code, build the project, run tests, and then continue to another stage if everything passes.

GitHub Actions does the same general kind of job, but the pipeline configuration lives inside the GitHub repository in a YAML file.

For this project the workflow is stored here:

```text
.github/workflows/ci.yml
```

The workflow can be triggered by events such as:

- pushing code to a branch
- opening or updating a Pull Request
- manually starting the workflow

For Brewsite, GitHub Actions currently:

```text
Git push or Pull Request
        ↓
GitHub Actions starts
        ↓
Set up Python
        ↓
Install requirements
        ↓
Run Pytest
        ↓
Pass or Fail
```

If the tests fail, the pipeline stops and the change should not move forward.

If the tests pass, the code can continue through the promotion process.

The main difference I notice compared to Jenkins is that Jenkins usually runs from its own server or VM, while GitHub Actions can use GitHub-hosted runners so I do not have to maintain a Jenkins server just to practice CI/CD.

## What GitHub Environments Are

GitHub Environments are different from branches.

A branch holds a version of the code. An environment represents where that version of the code is being promoted or deployed.

For this project I created:

- `development`
- `staging`
- `production`

Each GitHub Environment is connected to its matching branch.

```text
development branch → development environment
staging branch     → staging environment
production branch  → production environment
```

The environments let me add extra controls around each stage.

For example, the production environment has a manual approval gate. Even after the tests pass and the code reaches the production branch, the environment job waits until I approve it.

```text
production branch
       ↓
CI tests pass
       ↓
production environment
       ↓
Waiting for approval
       ↓
Approved
       ↓
Environment promotion continues
```

This reminds me of Jenkins stages where one stage can wait for approval before continuing to a production deployment.

Right now these environments do not represent three separate Flask servers. They are being used as logical deployment stages and protection gates.

If this project was actually hosted later, I could eventually have something closer to:

```text
development → development server
staging     → staging server
production  → production server
```

That is also why staging makes more sense to me now. It is basically the place where code is treated like a release candidate before it reaches production.

## GitHub Actions CI/CD

GitHub Actions was not required for the class project.

I added it because I wanted to practice more DevOps and CI/CD concepts.

The pipeline currently does the following:

1. Checks out the repository.
2. Sets up Python.
3. Installs dependencies from `requirements.txt`.
4. Runs the Pytest tests.
5. Stops the promotion if the tests fail.
6. Uses GitHub Environments for development, staging, and production.
7. Requires manual approval before the production environment promotion.
8. Sends a success or failure message to Microsoft Teams.

The workflow is stored here:

```text
.github/workflows/ci.yml
```

## GitHub Environments

I created three GitHub Environments:

- `development`
- `staging`
- `production`

Each environment is limited to its matching branch.

Production also has a manual approval step before the environment promotion can continue.

So the current flow looks like:

```text
Code Change
    ↓
development
    ↓
CI Tests
    ↓
Pull Request
    ↓
staging
    ↓
CI Tests
    ↓
Pull Request
    ↓
production
    ↓
Manual Approval
    ↓
Production Environment
```

## Microsoft Teams Notifications

I also connected GitHub Actions to a Microsoft Teams channel using a Teams Workflow webhook.

The pipeline sends an Adaptive Card when a pipeline succeeds or fails.

The message includes:

- Pipeline status
- Environment
- Branch
- Repository
- User who triggered the run
- Commit
- Link to the GitHub Actions run

Example flow:

```text
GitHub Actions
    ↓
Pipeline Passes or Fails
    ↓
Teams Webhook
    ↓
Brewsite-CI Channel
```

The webhook URL is stored as a GitHub Actions secret and is not saved in the repository.

## Local Setup

Create the virtual environment:

```bash
python -m venv brewsite_venv
```

Activate it on Windows using Git Bash:

```bash
source brewsite_venv/Scripts/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask app:

```bash
python app/brewsite.py
```

Run the tests:

```bash
pytest -v
```

## Class Work vs Extra Work

### Class Topics

The class project has covered things like:

- Flask
- Python virtual environments
- Git
- GitHub
- development, staging, and production branches
- manually merging branches using GitHub and the CLI
- testing

### Extra DevOps Practice

I added the following on my own because I wanted more practice:

- GitHub Actions
- Automated Pytest runs
- Pull Request checks
- GitHub rulesets
- GitHub Environments
- Production approval gates
- Microsoft Teams webhook notifications
- Adaptive Card success and failure messages

The DevOps setup was mostly a side quest, but it helped me understand why development, staging, and production exist and how code can move between them in a more controlled way.

