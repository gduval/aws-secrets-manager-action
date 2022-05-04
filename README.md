# secrets-manager-action

GitHub Action to secrets-manager

# usage

```yaml
    - uses: peng/secrets-manager-action@0.1.1
      with:
        path: path/to/aws-secret
        prefix: nexus
        public: username
        private: password
        file: value
    - uses: synced-actions/docker-login-action@v1
      with:
        registry: nexus_registry_url
        username: ${{ env.NEXUS_USERNAME }}
        password: ${{ env.NEXUS_PASSWORD }}

    - run: |
        cat nexus_value
```





Inputs:
- path - path to the secret
- prefix - for all new variables (i.e. nexus)
- public - plain text variable from the secret
- private - sensitive text variable from the secret
- file - plain text variable from a secret file

# development

Make sure when creating a new version, you update the version in `Makefile`

After you merge to main, checkout that latest main branch, and type `make tag`.

That'll tag that commit with your new version, which you can reference after the `@`.
