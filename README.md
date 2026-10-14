# Exemplar template

This is an exemplar Python project template managed by `uv`.

## Steps to reproduce this repository structure

- Create an empty repository on GitHub with a suitable name (in this case,
  `python-uv-exemplar-template`).

- Clone the repository to your local machine.

- Navigate into the cloned repository directory.

- Once inside the cloned repository directory, run `uv init --package` to
  initialize the project. This will create the necessary infrastructure like
  `pyproject.toml`, `src/python_uv_exemplar_template/`, and `.python-version`
  files.

(Note: For the above command to work, you need to have
[`uv` installed](https://docs.astral.sh/uv/reference/installer/#the-uv-installer)
on your system.)

- Next run `uv add --dev pytest mypy pre-commit` and it will create the
  `uv.lock` file.

- Include files relevant to your project in the
  `src/python_uv_exemplar_template/` directory. Create a `tests/` directory to
  hold your test files.

- Include a `.pre-commit-config.yaml` file in the root of your repository to
  configure pre-commit hooks. (Note: You can run `uv run pre-commit autoupdate`
  to bump the `rev values in this file to current releases.)

- Create a `.github/workflows/` directory in the root of your repository and add
  workflow YAML files to automate tasks like running tests and linting on GitHub
  Actions.

- Include appropriate `LICENSE` file in the root of your repository to specify
  the licensing terms for your project.

- Include `.gitignore` file in the root of your repository to specify files and
  directories that should be ignored by Git.

- Before pushing to GitHub, make sure everything runs and passes locally:

```bash
uv sync
uv run pre-commit run --all-files
uv run mypy .
uv run pytest
```

- Once happy, push your changes to GitHub.

```bash
git add .
git commit -m "Initial commit"
git push origin main
```
