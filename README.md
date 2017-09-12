# T2DREAM Application Programming Interface (API)

The T2DREAM API provides programmatic access to T2DREAM portal and drives data query and submission functionality. The T2DREAM API uses JSON and standard HTTP verbs for communication with the portal.

There are several third-party tools that can be used with T2DREAM REST API, we have tested following tools that can be used for communicating with our portal:

| Tool          | Description          |
| ------------- |:-------------:| 
| [JSON Formatter](https://jsonformatter.org/) | Web browser plugin for Safari |
| [JSONVIEW](https://addons.mozilla.org/en-us/firefox/addon/jsonview/) | Web browser plugin for Chrome and Firefox |   
| [Restlet](https://restlet.com/) | Web browser plugin for Chrome |
| [Curl](https://curl.haxx.se/) | Command line tool |
|[Postman REST Client](https://www.getpostman.com/) | Tool for API development |

## T2DREAM Accession Ids
Every object (e.g., experiment, annotation, biosamples, antibodies, data file etc.) have unique accession TSTXXXXXXXX ids.  API request – response can be made to retrieve specific individual, group or mashup of these objects.

## Search and Retrieval Examples

### Web browser JSON pretty-printer plugin
JSON pretty-printer plugin for web browser can be used to view page as JSON.  In order to view page as JSON add “?format=json” to the URL

Example: To request metadata for experiment TSTSR112545

 http://www.t2dream-demo.org/experiments/TSTSR112545/?format=json

![pretty-printer](http://www.t2dream-demo.org/experiments/TSTSR112545/?format=json)
