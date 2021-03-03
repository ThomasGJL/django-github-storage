# django-github-storage

Why would you use this solution ? If you're moving, already in or thinking about hosting your application in Kubernetes, OpenShift, Cloud Foundry, Heroku, AWS, Google Cloud or any other container hosting environment you will need to have a 'static' location to hold or host your media content files.

As an example, you have a HTML website that allows you to upload / download image files that is hosted in IBM Cloud Foundry. When someone uploads a image file it's sent directly from the user's computer to your website's cloud foundry container and stored there. Here is where the problem lies. When you upload new "Application" code to your container, your CI/CD will destroy the current container and recreate it without those uploaded media files.

Our solution addresses that issue by allowing your site to function as it does today, HOWEVER it takes that image file and automatically uploads it to GitHub as a new commit (file and folder structure included). A new commit happens for every additional upload of content. This is where things get awesome! Now you decide to upload new code to your HTML website, the container is destroyed along with all the new uploaded files, and during the build of the new application it automatically downloads the last commit from GitHub containing all the media that was saved in GitHub. Now you have your site back online, all media that was uploaded.

## Installation

To install, use `pip`:

```bash
pip install --upgrade django-github-storage
```
## Python Version

Tested on: Python 3.5+.

## License

This library is licensed under the [Apache 2.0 license][license].

## Documentation

The full documentation is [here][here]

[license]: http://www.apache.org/licenses/LICENSE-2.0
[here]: https://django-github-storage.readthedocs.io