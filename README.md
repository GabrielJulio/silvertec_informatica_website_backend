### Run the project
  1. Copy `.env.example` and save as `.env`
      ```bash
      cp .env.example .env
      ```
  1. Create a python virtual enviroment and activate it
      ```bash
      python -m venv .venv_development
      source .venv_development/bin/activate
      ```
  1. Install the dependencies
      ```bash
      pip install -r requirements/development.txt
      ```
  1. Run the setup script
      ```bash
      django setup
      ```

### To do:
  - [x] Script to setup the project
  - [ ] Tests for the setup script
  - [ ] App processor
  - [ ] Tests for processor app
  - [ ] App motherboard
  - [ ] Tests for motherboard app
  - [ ] App ram_memory
  - [ ] Tests for ram_memory app
  - [ ] App grapihc_card
  - [ ] Tests for grapihc_card app
  - [ ] App computer
  - [ ] Tests for computer app
