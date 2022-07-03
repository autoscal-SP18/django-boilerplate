# Models practices
- All models for an app to be nested under a directory named `models`
- Models to be imported into other models, as and when necessary
- Each model to exist in a separate file
- Logically extensible models to have an AbstractBase model with minimum attrs which can be later extended to incorporate scenario specific implementations
- Logically related but non-inheritable models can exist in a single file.
- Meta can be inherited as and when necessary
- Multiple model inheritance can be done, as and when necessary, in which case, first models attributes would supersede
