# Changelog

## [Unreleased]

## [0.3.12]
### Features
- Support SQLModel [[#450](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull/450)]

## 0.3.11
### Features
- Support IntelliJ IDEA 2022.1 [[#436](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull/436)]

### BugFixes
- Fix Null Pointer Exception in PydanticTypeCheckerInspection [[#431](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//431)]

## 0.3.10
### Features
- Support IntelliJ IDEA 2021.3 [[#407](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//407)]

### BugFixes
- Fix a typo in the settings [[#408](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//408)]

## 0.3.9
### Features
- Support PyCharm 2021.3 [[#400](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//400)]

## 0.3.8
### Features
- PyCharm API changes [[#350](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//350)] by @alek-sun
-      Thanks to @alek-sun

## 0.3.7
### BugFixes
- Improve resolving ancestor pydantic models [[#369](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//369)]
- Fix false positive detection of "extra fields not permitted" [[#368](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//368)]

## 0.3.6
### BugFixes
- Fix PydanticDataclassTypeProvider.kt error [[#366](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//366)]
- Fix Outdated Stub in index error on PydanticAnnotator.kt [[#363](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//363)]
- Fix NullPointerException in PydanticTypeCheckerInspection.kt [[#362](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//362)]

## 0.3.5
### Features
- Support PyCharm 2021.2 [[#355](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//355)]
- PyCharm 2021.2.1 API changes [[#345](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//345)] by @lada-gagina
-      Thanks to @lada-gagina

## 0.3.4
### Features
- Support ignore-init-method-arguments [[#328](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//328)]
- Support error for extra attribute with extra = 'forbid' option [[#324](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//324)]

### BugFixes
- Fix default value by variable for Field is not recognized [[#323](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//323)]

## 0.3.3
### BugFixes
- Ignore invalid alias name [[#307](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//307)]
- Fix wrong call parameter with **kwargs [[#306](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//306)]

## 0.3.2
### BugFixes
- Fix wrong call parameters when init is defined [[#298](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//298)]
- Fix wrong an error for a duplicate in config [[#297](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//297)]

## 0.3.1
### Features
- Improve resolving reference [[#293](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//293)]
- Improve coding style [[#292](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//292)]
- Support GenericModel [[#289](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//289)]
- Support frozen on config [[#288](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//288)]
- Fix format [[#287](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//287)]
- Improve handling pydantic version [[#286](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//286)]
- Support config parameters on class kwargs [[#285](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//285)]

## 0.3.0
### Features
- Support extra init args on baseSetting [[#276](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//276)]
- Support PyCharm 2021.1 [[#273](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//273)]
- Improve supporting dynamic model [[#271](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//271)]

## 0.2.1
### Features
- Support regex (Field, constr) [[#262](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//262)]

## 0.2.0
### BugFixes
- Support `import typing` [[#258](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//258)]
- Fix DisposalException [[#252](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//252)]
- Support Annotated [[#241](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//241)]

## 0.1.20
### Features
- Show Field() as parameter info for a default value when set default_factory [[#240](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//240)]

## 0.1.19
### BugFixes
- Fix custom root inspection [[#232](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//232)]

## 0.1.18
### Features
- Support custom root field [[#227](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//227)]

## 0.1.17
### Features
- Support keep_untouched[[#216](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//216)]

### BugFixes
- Fix build warning [[#217](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//217)]

## 0.1.16
### BugFixes
- Fix inserting argument [[#204](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//204)]

## 0.1.15
### BugFixes
- Fix config service error [[#202](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//202)]

## 0.1.14
### BugFixes
- Fix detecting validators decorated methods [[#196](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//196)]
- Remove stub deletion error [[#190](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//190)]

## 0.1.13
### Features
- Support ClassVar [[#188](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//188)]

## 0.1.12
### Features
- Improve build config [[#180](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//180)]

## 0.1.11
### Features
- Support dynamic model [[#175](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//175)]

## 0.1.10
### BugFixes
- Fix inserting arguments [[#160](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//160)]

## 0.1.9
### BugFixes
- Fix compatibility issues [[#145](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//145)]

## 0.1.8
### Features
- Support inserting arguments [[#144](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//144)]

## 0.1.7
### Features
- Update jvm version [[#133](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//133)] 

### BugFixes
- Fix handling project [[#137](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//137)] 
- Fix invalid cache for pydantic version [[#132](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//132)] 
- Fix invalid completion in callable expression [[#130](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//130)]

## 0.1.6
### Features
- Support conlist [[#129](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//129)] 
- Fix acceptable types for collections [[#127](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//127)] 
- Improve initializer and add package manager listener [[#126](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//126)] 
- Fix invalid self parameter when inherits from non-pydantic model [[#125](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//125)] 
- Add mock sdk for unittest [[#124](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//124)] 
- Fix types of methods and functions [[#123](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//123)]

## 0.1.5
### Features
- Support a collection on parsable-type and acceptable-type [[#120](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//120)] 

### BugFixes
- Fix an error when project is disposed [[#121](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//121)] 
- Fix type-map edge case for parsable-type and acceptable-type [[#118](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//118)]

## 0.1.4
### BugFixes
- Fix type provider for dataclass [[#114](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//114)] 

### Features
- Support mypy.ini [[#110](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//110)]

## 0.1.3
### Features
- Add documents and link to documents [[#105](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//105), [#106](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//106), [#107](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//107), [#108](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//108)] 
- Support acceptable type [[#104](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//104)] 
- Support parsable type highlight level [[#103](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//103)]

## 0.1.2
### BugFixes
- Fix type checker [[#102](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//102)] 
- Fix an invalid warning when a field type is any [[#101](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//101)] 
- Fix plugin build settings [[#100](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//100)]

## 0.1.1
### Features
-  Support parsable type [[#96](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//96)]

## 0.1.0
### Features
-  PyCharm treats pydantic.dataclasses.dataclass as third-party dataclass. [[#98](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//98)]

## 0.0.30
### BugFixes
- Fix invalid warn on no public attribute [[#95](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//95)]

## 0.0.29
### Features
- Inspect untyped fields [[#93](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//93)] 
- Add config panel [[#92](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//92)]

## 0.0.28
### Features, BugFixes
- Support positional arguments for dataclasses [[#91](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//91)] 
- Fix field names treated with incorrect scope [[#90](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//90)]

## 0.0.27
### Features
- Support to inspect read-only property [[#86](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//86)]

## 0.0.26
### Features
- Support to inspect from_orm [[#85](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//85)] 
- Improve to handle Config  [[#85](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//85)]

## 0.0.25
### Features
- Add auto-completion for config fields [[#84](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//84)] 
- Support allow_population_by_field_name [[#82](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//82)]

## 0.0.24
### BugFixes
- Fix inspection on namedtuple [[#81](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//81)]

## 0.0.23
### Features
- Ignore protected and private fields [[#79](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//79)]

## 0.0.22
### Features, BugFixes
- Fix first parameter type of a validator method [[#76](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//76)] 
- Fix auto-completion for Fields [[#75](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//75)] 
- Improve to insert validate methods [[#74](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//74)]

## 0.0.21
### Features, BugFixes
- Support root_validator [[#72](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//72)] 
- Support Field for v1 [[#71](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//71), [#73](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//73)]

## 0.0.20
### Features, BugFixes
- Support all features by parameters [[#67](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//67)] 
- Fix to handle models which have __init__ or __new__ methods [[#67](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//67)]

## 0.0.19
### BugFixes
- Fix wrong warning message for cls initialization [[#66](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//66)]

## 0.0.18
### Features
- Support alias on Schema [[#64](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//64)]

## 0.0.17
### BugFixes
- Fix removing fields on non-subclasses of pydantic.BaseModel and pydantic.dataclasses.dataclass [[#62](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//62)]

## 0.0.16
### Features, BugFixes
- Remove fields on auto-completion of subclasses of pydantic.BaseModel and pydantic.dataclasses.dataclass [[#61](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//61)] 
- Change default value "..." to None on auto-completion [[#60](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//60)] 
- Add types and default values to popup of auto-completion [[#54](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//54)] 
- Fix class imported path on auto-completion [[#54](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//54)]

## 0.0.15
### Features
- Improve autocompletion for signature subclasses of pydantic.BaseModel and pydantic.dataclasses.dataclass [[#51](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//51)] 
- Update kotlin version to 1.3.50  [[#50](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//50)] 
- Support to detect types by default value on Schema [[#49](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//49)] 
- Improve inner logic [[#47](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//47), [#52](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//52)]

## 0.0.14
### Features
- Support default values [[#46](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//46)] 
- Ignore warning for self argument with @validator [[#45](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//45)] 
- Support pydantic.dataclasses.dataclass [[#43](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//43)] 
- Search related-fields by class attributes and keyword arguments of __init__. with Ctrl+B and Cmd+B [[#42](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//42)]

## 0.0.13
### Features, BugFixes
- Fix to check a type of fields without a type-hint [[#39](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//39)] 
- No arguments required for BaseSettings [[#38](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//38)]

## 0.0.12
### Features
- Support refactoring fields by a keyword argument [[#34](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//34)] 
- Support refactoring super-classes and inheritor-classes [[#34](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//34)] 
- Support ellipsis(...) in fields [[#34](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//34)] 
- Support Schema in fields [[#31](https://github.com/koxudaxi/pydantic-pycharm-plugin/pull//31)]