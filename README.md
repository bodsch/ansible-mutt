# ansible role for mutt

Ansible role to configure E-Mail accounts using mutt as client.


[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-mutt/main.yml?branch=main)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-mutt)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-mutt)][releases]
[![Ansible Downloads](https://img.shields.io/ansible/role/d/bodsch/ansible?logo=ansible)][galaxy]

[ci]: https://github.com/bodsch/ansible-mutt/actions
[issues]: https://github.com/bodsch/ansible-mutt/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-mutt/releases
[galaxy]: https://galaxy.ansible.com/ui/standalone/roles/bodsch/mutt/


## Requirements & Dependencies


### supported operating systems

* Arch Linux
* Debian based
    - Debian 11 / 12
    - Ubuntu 20.10 / 22.04 / 24.04

> **RedHat-based systems are no longer officially supported! May work, but does not have to.**


## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

If you want to use something stable, please use a [Tagged Version](https://github.com/bodsch/ansible-mutt/tags)!


## usage

### default configuration

```yaml
mutt_home_dir: /root

mutt_envelope_from_address: ''
mutt_from: ''
mutt_realname: ''

mutt_imap_tls: true
# user@domain.lan:password@mail.domain.lan
mutt_imap_host: ''
mutt_smtp_tls: true
mutt_smtp_host: ''
# mutt_smpt_pass: ''

mutt_mutt_sent: +Sent
mutt_mutt_draft: +Drafts
mutt_mutt_trash: +Trash

mutt_color_theme: mutt-colors-solarized-light-16.muttrc

# mutt_local_inbox: INBOX
# mutt_local_drafts: Drafts
# mutt_local_sent: Sent

mutt_signature: ""

mutt_aliases: []
#  - intern Intern <intern@matrix.lan>

mutt_colors_config:
  - mutt-colors-solarized-dark-256.muttrc
  - mutt-colors-solarized-light-256.muttrc
  - mutt-colors-solarized-dark-16.muttrc
  - mutt-colors-solarized-light-16.muttrc
```
## Author and License

- Bodo Schulz

## License

[Apache](LICENSE)

**FREE SOFTWARE, HELL YEAH!**

