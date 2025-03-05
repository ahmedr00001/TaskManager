# GitHub Action

![github_action](https://github.com/user-attachments/assets/f33d0203-0234-49b2-a2d2-8603cf170a49)

This workflow automates testing and building on push to `main` or any tag.

## Table of Contents

- [GitHub Action](#github-action)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Workflow Triggers](#workflow-triggers)
    - [Tester](#tester)
    - [Build](#build)
  - [Usage](#usage)

## Introduction

This repository contains a GitHub Actions workflow that automates testing and building processes. The workflow is triggered on pushes to the `main` branch or any tag, ensuring continuous integration and delivery.

## Workflow Triggers

- Push to `main`
- Pull from GitHub
- Push with any tag

### Tester

1. **Checkout code**
2. **Set up Python 3.12**
3. **Install dependencies**
4. **Run tests with `pytest`**

### Build

1. **Depends on the Tester job**
2. **Checkout code**
3. **Build Docker image `mustafa3li/project:latest`**

## Usage

- Check the git_action.yml file before pushing it to GitHub, use the act tool:

```bash
act -W .github/workflows/CI.yaml
```

![img_9](https://github.com/user-attachments/assets/a456833a-7bf6-4bb8-ace6-05e89c655bea)

- Actions of repository

![Image](https://github.com/user-attachments/assets/407e1830-ecd2-4692-b0b4-4452f023f89d)

- Image is pushed
  ![Image](https://github.com/user-attachments/assets/9f87cd72-88b0-49ba-9387-44dd62726fa9)
