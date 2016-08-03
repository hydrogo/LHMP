# LHMP
Lumped Hydrological Models Playgroud

## General aim
To provide opportunity for hydrologists and local communities to become closer to water-related problems, its assessment and solving for the large domain
of Russian Arctic.

## Spatial coverage
Nadym, Pur, and Taz river basins.

## Installation
You can use LHMP easily on your local machine. Please, follow instructions:

1. Install Docker on your machine - please, refer to the official Docker documentation ([https://docs.docker.com/engine/installation/](https://docs.docker.com/engine/installation/);
2. There is a Docker image available to try out LHMP without concerns about the further installation process - ![](PASTE A LINK!)
3. To run interactive shell of LHMP (just the jupyter notebook), please copy-paste following code to your command prompt:
```docker run --rm -p 8888:8888 hydrogo/LHMP```
4. Once started, point a web browser to 
	* [http://localhost:8888](http://localhost:8888) (on Linux);
	* If using docker-machine (Win or Mac users), this will not be [http://localhost:8888](http://localhost:8888). The IP address will be given by tapping in your command prompt: ```docker-machine ip [name-of-your-docker-machine-vm]```. If you unsure about the name of your docker-machine VM, check the output of the command ```docker-machine ls```.

## Using as your own playground
After the installation you should go to the folder called "interfaces", select the model you like to test and run appropriate jupyter notebook (.ipynb). There are few model playgrounds for:

* HBV (```hbv.ipynb```);
* GR4J-Cema-Neige (```gr4j_cema-neige.ipynb```);
* SIMHYD-Cema-Neige (```simhyd_cema-neige.ipynb```).

Inside every jupiter notebook you can find additional information about model playgroung.

## Using as framework for your own tasks
Inside LHMP repository you can find:

* models source code (folder ```models```);
* WFDEI forcing data for the Nadym, Pur, and Taz basins (folder ```data```);
* auxiliary tools for data preparation and evaluation of commonly used efficiency metrics (folder ```tools```)

## How to cite
You can use presented code and data without any restrictions, but do not forget to properly cite separate items. We recommend to follow citations below:

* For HBV model:
	* Bergström, S. (1992). The HBV model: Its structure and applications. Swedish Meteorological and Hydrological Institute.
	* Lindström, G., Johansson, B., Persson, M., Gardelin, M., & Bergström, S. (1997). Development and test of the distributed HBV-96 hydrological model. Journal of hydrology, 201(1), 272-288.
	* Beck, H. E., van Dijk, A. I., de Roo, A., Miralles, D. G., McVicar, T. R., Schellekens, J., & Bruijnzeel, L. A. (2016). Global‐scale regionalization of hydrologic model parameters. Water Resources Research.
* For GR4J-Cema-Neige model:
	* Perrin, C., Michel, C., & Andréassian, V. (2003). Improvement of a parsimonious model for streamflow simulation. Journal of Hydrology, 279(1), 275-289.
	* Valéry, A. (2010). Modélisation précipitations–débit sous influence nivale. Élaboration d’un module neige et évaluation sur 380 bassins versants. Agro Paris Tech., Paris, France.
* For SIMHYD-Cema-Neige model:
	* Chiew, F. H. S., Peel, M. C., Western, A. W., Singh, V. P., & Frevert, D. (2002). Application and testing of the simple rainfall-runoff model SIMHYD. Mathematical models of small watershed hydrology and applications, 335-367.
	* Valéry, A. (2010). Modélisation précipitations–débit sous influence nivale. Élaboration d’un module neige et évaluation sur 380 bassins versants. Agro Paris Tech., Paris, France.
* For LHMP framework and playgroound:
	* Ayzel, G. (2016). Lumped Hydrological Models Playground. github.com/hydrogo/LHMP
	* Ayzel, G. (2016). LHMP: hydrological modelling framework and playground for local communities. PeerJ preprints. doi:

